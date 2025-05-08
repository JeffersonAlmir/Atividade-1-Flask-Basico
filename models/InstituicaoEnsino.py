class InstituicaoEnsino:
    
    def __init__(self,co_entidade, co_regiao, no_regiao, no_uf, sg_uf, no_municipio, 
    no_mesorregiao, no_microrregiao, no_entidade, qt_mat_bas, qt_mat_inf, qt_mat_fund, qt_mat_med, 
    qt_mat_med_ct, qt_mat_med_nm, qt_mat_prof, qt_mat_prof_tec, qt_mat_eja, qt_mat_esp):
        
        self.co_entidade = co_entidade
        self.co_regiao = co_regiao
        self.no_regiao = no_regiao
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.no_municipio = no_municipio
        self.no_mesorregiao = no_mesorregiao
        self.no_microrregiao = no_microrregiao
        self.no_entidade = no_entidade
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.qt_mat_med_ct = qt_mat_med_ct
        self.qt_mat_med_nm = qt_mat_med_nm
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_prof_tec = qt_mat_prof_tec
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp

    def toDict(self):
        return {
        "co_entidade": self.co_entidade,
        "co_regiao": self.co_regiao,
        "no_regiao": self.no_regiao,
        "no_uf": self.no_uf,
        "sg_uf": self.sg_uf,
        "no_municipio": self.no_municipio,
        "no_mesorregiao": self.no_mesorregiao,
        "no_microrregiao": self.no_microrregiao,
        "no_entidade": self.no_entidade,
        "qt_mat_bas": self.qt_mat_bas,
        "qt_mat_inf": self.qt_mat_inf,
        "qt_mat_fund": self.qt_mat_fund,
        "qt_mat_med": self.qt_mat_med,
        "qt_mat_med_ct": self.qt_mat_med_ct,
        "qt_mat_med_nm": self.qt_mat_med_nm,
        "qt_mat_prof": self.qt_mat_prof,
        "qt_mat_prof_tec": self.qt_mat_prof_tec,
        "qt_mat_eja": self.qt_mat_eja,
        "qt_mat_esp": self.qt_mat_esp
        } 