import pandas as pd
import numpy as np


class account(object):
    def __init__(self, 
                title = None, # string
                tag = None, # string tuple
                mtrt = 0, # int
                add_scdd_ipt = pd.Series([0], index=[0]), # Series
                sub_scdd_ipt = pd.Series([0], index=[0]), # Series
                note = ""): # string
        self.title = title
        self.tag = tag
        self.mtrt = mtrt
        self.add_scdd_ipt = add_scdd_ipt
        self.sub_scdd_ipt = sub_scdd_ipt
        self.note = note
        self.setdf()
        self.setjnl()
        
    #### INITIAL SETTING ####
    def setdf(self):
        self.dfcol = ['add_scdd', 'add_scdd_cum', 'sub_scdd', 'sub_scdd_cum', 'bal_strt', 'amt_add', 'amt_sub', 'bal_end', 'amt_rsdl']
        self.dfidx = np.arange(-1, self.mtrt + 1)
        self.df = pd.DataFrame(np.zeros([len(self.dfidx), len(self.dfcol)]), columns=self.dfcol, index=self.dfidx)
        self.df.loc[self.add_scdd_ipt.index, 'add_scdd'] = self.add_scdd_ipt
        self.df.loc[self.sub_scdd_ipt.index, 'sub_scdd'] = self.sub_scdd_ipt
        self._cal_bal()
        
    def setjnl(self):
        self.jnlcol = ['amt_add', 'amt_sub', 'note']
        self.jnlidx = [-1]
        self.jnl = pd.DataFrame(np.zeros([len(self.jnlidx), len(self.jnlcol)]), columns=self.jnlcol, index=self.jnlidx)
    #### INITIAL SETTING ####
    
    #### INPUT DATA ####
    def addamt(self, index, amt, note=""):
        tmpjnl = pd.DataFrame([[amt, 0, note]], columns=self.jnlcol, index=[index])
        self.jnl = pd.concat([self.jnl, tmpjnl])
        
        self.df.loc[index, 'amt_add'] += amt
        self._cal_bal()
        
    def subamt(self, index, amt, note=""):
        tmpjnl = pd.DataFrame([[0, amt, note]], columns=self.jnlcol, index=[index])
        self.jnl = pd.concat([self.jnl, tmpjnl])
        
        self.df.loc[index, 'amt_sub'] += amt
        self._cal_bal()
    def calamt(self, index, amt, note=""):
        if amt >= 0:
            self.addamt(index, amt, note)
        else:
            self.subamt(index, -amt, note)
    #### INPUT DATA ####
    
    #### OUTPUT DATA ####
    def bal_strt(self, idx=None):
        if idx is None:
            return self.df.loc[:, 'bal_strt']
        else:
            return self.df.loc[idx, 'bal_strt']
        
    def bal_end(self, idx=None):
        if idx is None:
            return self.df.loc[:, 'bal_end']
        else:
            return self.df.loc[idx, 'Bal_end']
        
    def add_scdd(self, idx=None):
        if idx is None:
            return self.df.loc[:, 'add_scdd']
        else:
            return self.df.loc[idx, 'add_scdd']
        
    def sub_scdd(self, idx=None):
        if idx is None:
            return self.df.loc[:, 'sub_scdd']
        else:
            return self.df.loc[idx, 'sub_scdd']
    
    def amt_rsdl(self, idx=None):
        if idx is None:
            return self.df.loc[:, 'amt_rsdl']
        else:
            return self.df.loc[idx, 'amt_rsdl']
    #### OUTPUT DATA ####
    
    #### CALCULATE DATA ####
    def _cal_bal(self):
        self.df.loc[:, 'add_scdd_cum'] = self.df.loc[:, 'add_scdd'].cumsum()
        self.df.loc[:, 'sub_scdd_cum'] = self.df.loc[:, 'sub_scdd'].cumsum()
        
        self.df.loc[-1, 'bal_end'] = self.df.loc[-1, 'bal_strt'] + self.df.loc[-1, 'amt_add'] \
                                     - self.df.loc[-1, 'amt_sub']
        for idx in np.arange(0, self.mtrt + 1):
            self.df.loc[idx, 'bal_strt'] = self.df.loc[idx-1, 'bal_end']
            self.df.loc[idx, 'bal_end'] = self.df.loc[idx, 'bal_strt'] + self.df.loc[idx, 'amt_add'] \
                                          - self.df.loc[idx, 'amt_sub']
        self.df.loc[:, 'amt_rsdl'] = self.df.loc[:, 'add_scdd_cum'] - self.df.loc[:, 'sub_scdd_cum'] \
                                     - self.df.loc[:, 'bal_end']
    #### CALCULATE DATA ####
    
    
class accmerge(object):
    def __init__(self, accdct):
        self.accdct = accdct # dictionary
    
    def df(self, var='amt_scdd'):
        tmp_dct = pd.DataFrame({x: self.accdct[x].df.loc[:, var] for x in self.accdct})
        return tmp_dct
    
    def title(self):
        tmp_dct = pd.Series({x: self.accdct[x].title for x in self.accdct})
        return tmp_dct
    
    def tag(self):
        tmp_dct = pd.Series({x: self.accdct[x].tag for x in self.accdct})
        return tmp_dct
    
    def mtrt(self):
        tmp_dct = pd.Series({x: self.accdct[x].mtrt for x in self.accdct})
        return tmp_dct
    
    def note(self):
        tmp_dct = pd.Series({x: self.accdct[x].note for x in self.accdct})
        return tmp_dct