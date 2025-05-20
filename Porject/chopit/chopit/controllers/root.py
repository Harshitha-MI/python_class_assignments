# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound

from chopit.lib.base import BaseController
from chopit.controllers.error import ErrorController
from chopit.model.chop import *
import tw2.forms as twf
from tg import validate
from formencode import validators, compound, schema


__all__ = ['RootController']


class SearchFormValidator(schema.Schema):
    query = compound.All(validators.Regex(r'^ *[A-Z]* *$'),
                         validators.PlainText(),
                         validators.String(min=3,strip=True))
    enzyme  = validators.OneOf(["Trypsin","Lys C","Lys N","Glu C (bicarbonate)",
                                "Glu C (phosphate)"])
    miss_cleavage = validators.OneOf(["0","1","2"])
    minlen = validators.Int(min=1)
    maxlen = validators.Int(min=1)
    minwt = validators.Int(min=1)
    maxwt = validators.Int(min=1)   



class SearchForm(twf.Form):
    class child(twf.TableLayout):
        query = twf.TextArea(label="Protein Sequence",
                              rows=8,cols=45,
                              attrs={'title':'Please paste your protein sequence here'})
        enzyme = twf.SingleSelectField(label="Enzyme",
                                     options=["Trypsin",
                                              "Lys C",
                                              "Lys N",
                                              "Glu C (bicarbonate)",
                                              "Glu C (phosphate)"],
                                     prompt_text=None)
        miss_cleavage = twf.SingleSelectField(label="Miss Cleavage",
                                     options=["0",
                                              "1",
                                              "2"],
                                     prompt_text=None)
        minlen = twf.TextField(label="Min Length",
                               attrs = {'style':'width: 50px;'})
        maxlen = twf.TextField(label="Max Length",
                               attrs = {'style':'width: 50px;'})
        minwt = twf.TextField(label="Min Molecular Weight",
                              attrs = {'style':'width: 50px;'})
        maxwt = twf.TextField(label="Max Molecular Weight",
                              attrs = {'style':'width: 50px;'})
        
        css_class = 'table'
        attrs = {'style': 'width: 800px;'}

    action = '/search'
    submit = twf.SubmitButton(value="Chop")
    validator= SearchFormValidator

class RootController(BaseController):

    @expose('chopit.templates.index')
    def index(self,**kwargs):
        return dict(title = "Chop It!",
                    form=SearchForm)
        
    @expose('chopit.templates.search')
    @validate(SearchForm, error_handler=index)
    def search(self,query,enzyme,miss_cleavage,minlen,maxlen,minwt,maxwt):
        miss_cleavage = int(miss_cleavage)
        minlen = int(minlen)if minlen != None and minlen != '' else 0
        maxlen = int(maxlen)if maxlen != None and maxlen != '' else 0
        minwt = int(minwt)if minwt != None and minwt != '' else 0
        maxwt = int(maxwt)if maxwt != None and maxwt != '' else 0
        if enzyme == 'Trypsin':
            p = trypsin(query)
        elif enzyme == 'Lys C':
            p = lys_c(query)
        elif enzyme == 'Lys N':
            p = lys_n(query)
        elif enzyme == 'Glu C (bicarbonate)':
            p = glu_c_bicarb(query)
        elif enzyme == 'Glu C (phosphate)':
            p = glu_c_phos(query)
        peptides = p.filter(miss_cleavage,minlen,maxlen,minwt,maxwt)
        if not peptides:
            flash('No results found.Please reconsider your parameters.','error')
            redirect('http://localhost:8080/')   
        return dict(title="Chop It..!",peptides=peptides,query=query,enzyme=enzyme,
                    minlen=minlen,maxlen=maxlen,minwt=minwt,maxwt=maxwt)



