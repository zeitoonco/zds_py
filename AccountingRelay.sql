CREATE TABLE IF NOT EXISTS account (
  accountid             BIGINT                 NOT NULL,
  parentid              BIGINT,
  type                  INTEGER                NOT NULL,
  code                  CHARACTER VARYING(40)  NOT NULL,
  title                 CHARACTER VARYING(250) NOT NULL,
  title2                CHARACTER VARYING(250),
  isactive              BOOLEAN DEFAULT TRUE   NOT NULL,
  cashflowcategory      INTEGER,
  openingbalance        NUMERIC(19, 4),
  balancetype           INTEGER                NOT NULL,
  hasbalancetypecheck   BOOLEAN DEFAULT FALSE  NOT NULL,
  hasdl                 BOOLEAN                NOT NULL,
  hascurrency           BOOLEAN DEFAULT FALSE  NOT NULL,
  hascurrencyconversion BOOLEAN DEFAULT FALSE  NOT NULL,
  hastracking           BOOLEAN DEFAULT FALSE  NOT NULL,
  hastrackingcheck      BOOLEAN DEFAULT FALSE  NOT NULL,
  version               BIGINT                 NOT NULL DEFAULT 0,
  del                   BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE account_accountid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE account_accountid_seq OWNED BY account.accountid;

CREATE TABLE IF NOT EXISTS accountbalancetype (
  accountbalancetypeid INTEGER NOT NULL,
  cl                   CHARACTER VARYING(250),
  glsl                 CHARACTER VARYING(250)
);

CREATE SEQUENCE accountbalancetype_accountbalancetypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE accountbalancetype_accountbalancetypeid_seq OWNED BY accountbalancetype.accountbalancetypeid;


CREATE TABLE IF NOT EXISTS accounttopic (
  topicid   BIGINT NOT NULL,
  accountid BIGINT NOT NULL
);

CREATE TABLE IF NOT EXISTS bank (
  bankid  BIGINT                 NOT NULL,
  title   CHARACTER VARYING(250) NOT NULL,
  logo    BYTEA,
  version BIGINT                 NOT NULL DEFAULT 0,
  del     BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE bank_bankid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE bank_bankid_seq OWNED BY bank.bankid;

CREATE TABLE IF NOT EXISTS bankaccount (
  bankaccountid     BIGINT                   NOT NULL,
  bankbranchid      BIGINT                   NOT NULL,
  accountno         INTEGER                  NOT NULL,
  bankaccounttypeid BIGINT                   NOT NULL,
  dlid              BIGINT                   NOT NULL,
  currencyid        BIGINT                   NOT NULL,
  rate              NUMERIC(24, 16)          NOT NULL,
  firstamount       NUMERIC(19, 4)           NOT NULL,
  firstdate         TIMESTAMP WITH TIME ZONE NOT NULL,
  balance           NUMERIC(19, 4)           NOT NULL,
  billfirstamount   NUMERIC(19, 4),
  clearformatname   CHARACTER VARYING(250),
  owner             CHARACTER VARYING(4000),
  version           BIGINT                   NOT NULL DEFAULT 0,
  del               BOOLEAN DEFAULT FALSE    NOT NULL
);

CREATE SEQUENCE bankaccount_bankaccountid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE bankaccount_bankaccountid_seq OWNED BY bankaccount.bankaccountid;

CREATE TABLE IF NOT EXISTS bankaccounttype (
  bankaccounttypeid BIGINT                 NOT NULL,
  title             CHARACTER VARYING(250) NOT NULL,
  haschequebook     BOOLEAN                NOT NULL,
  version           BIGINT                 NOT NULL DEFAULT 0,
  del               BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE bankaccounttype_bankaccounttypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE bankaccounttype_bankaccounttypeid_seq OWNED BY bankaccounttype.bankaccounttypeid;

CREATE TABLE IF NOT EXISTS bankbranch (
  bankbranchid BIGINT                 NOT NULL,
  bankid       BIGINT                 NOT NULL,
  code         CHARACTER VARYING(250) NOT NULL,
  title        CHARACTER VARYING(250) NOT NULL,
  locationid   BIGINT                 NOT NULL,
  version      BIGINT                 NOT NULL DEFAULT 0,
  del          BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE bankbranch_bankbranchid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE bankbranch_bankbranchid_seq OWNED BY bankbranch.bankbranchid;

CREATE TABLE IF NOT EXISTS cash (
  cashid      BIGINT                   NOT NULL,
  title       CHARACTER VARYING(250)   NOT NULL,
  dlid        BIGINT                   NOT NULL,
  currencyid  BIGINT                   NOT NULL,
  rate        NUMERIC(26, 16)          NOT NULL,
  firstamount NUMERIC(19, 4)           NOT NULL,
  firstdate   TIMESTAMP WITH TIME ZONE NOT NULL,
  balance     NUMERIC(19, 4)           NOT NULL,
  version     BIGINT                   NOT NULL DEFAULT 0,
  del         BOOLEAN DEFAULT FALSE    NOT NULL
);

CREATE SEQUENCE cash_cashid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE cash_cashid_seq OWNED BY cash.cashid;

CREATE TABLE IF NOT EXISTS category (
  categoryid BIGINT                 NOT NULL,
  type       INTEGER                NOT NULL,
  title      CHARACTER VARYING(250) NOT NULL
);


CREATE SEQUENCE category_categoryid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE category_categoryid_seq OWNED BY category.categoryid;

CREATE TABLE IF NOT EXISTS categorytype (
  categorytypeid INTEGER                NOT NULL,
  title          CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE categorytype_categorytypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE categorytype_categorytypeid_seq OWNED BY categorytype.categorytypeid;

CREATE TABLE IF NOT EXISTS config (
  name     CHARACTER VARYING(255) NOT NULL,
  value    TEXT,
  version  BIGINT                 NOT NULL DEFAULT 0,
  configid BIGINT                 NOT NULL
);


CREATE SEQUENCE config_configid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE config_configid_seq OWNED BY config.configid;


CREATE TABLE IF NOT EXISTS costcenter (
  costcenterid BIGINT                NOT NULL,
  dlid         BIGINT                NOT NULL,
  type         INTEGER               NOT NULL,
  version      BIGINT                NOT NULL DEFAULT 0,
  del          BOOLEAN DEFAULT FALSE NOT NULL
);

CREATE SEQUENCE costcenter_costcenterid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE costcenter_costcenterid_seq OWNED BY costcenter.costcenterid;

CREATE TABLE IF NOT EXISTS costcentertype (
  costcentertypeid INTEGER                NOT NULL,
  title            CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE costcentertype_costcentertypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE costcentertype_costcentertypeid_seq OWNED BY costcentertype.costcentertypeid;


CREATE TABLE IF NOT EXISTS currency (
  currencyid      BIGINT                 NOT NULL,
  title           CHARACTER VARYING(250) NOT NULL,
  exchangeunit    INTEGER                NOT NULL,
  precisioncount  INTEGER                NOT NULL,
  precisionname   CHARACTER VARYING(40),
  precisionnameen CHARACTER VARYING(40),
  sign            CHARACTER VARYING(40)  NOT NULL,
  version         BIGINT                 NOT NULL DEFAULT 0,
  del             BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE currency_currencyid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE currency_currencyid_seq OWNED BY currency.currencyid;


CREATE TABLE IF NOT EXISTS currencyexchangerate (
  currencyexchangerateid BIGINT NOT NULL,
  currencyid             BIGINT NOT NULL,
  effectivedate          TIMESTAMP WITH TIME ZONE,
  exchangerate           NUMERIC(24, 16),
  version                BIGINT NOT NULL DEFAULT 0,
  fiscalyearid           BIGINT NOT NULL
);

CREATE SEQUENCE currencyexchangerate_currencyexchangerateid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE currencyexchangerate_currencyexchangerateid_seq OWNED BY currencyexchangerate.currencyexchangerateid;


CREATE TABLE IF NOT EXISTS dl (
  dlid     BIGINT                 NOT NULL,
  code     CHARACTER VARYING(40)  NOT NULL,
  title    CHARACTER VARYING(250) NOT NULL,
  title2   CHARACTER VARYING(250),
  type     INTEGER                NOT NULL,
  isactive BOOLEAN DEFAULT TRUE   NOT NULL,
  version  BIGINT                 NOT NULL DEFAULT 0,
  del      BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE dl_dlid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE dl_dlid_seq OWNED BY dl.dlid;


CREATE TABLE IF NOT EXISTS dltype (
  dltypeid INTEGER                NOT NULL,
  title    CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE dltype_dltypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE dltype_dltypeid_seq OWNED BY dltype.dltypeid;


CREATE TABLE IF NOT EXISTS fiscalyear (
  fiscalyearid BIGINT                 NOT NULL,
  title        CHARACTER VARYING(250) NOT NULL,
  startdate    DATE                   NOT NULL,
  enddate      DATE                   NOT NULL,
  status       INTEGER                NOT NULL,
  version      BIGINT                 NOT NULL DEFAULT 0,
  del          BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE fiscalyear_fiscalyearid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE fiscalyear_fiscalyearid_seq OWNED BY fiscalyear.fiscalyearid;


CREATE TABLE IF NOT EXISTS glvoucher (
  glvoucherid  BIGINT                                 NOT NULL,
  number       INTEGER                                NOT NULL,
  "Date"       TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  fiscalyearid BIGINT                                 NOT NULL,
  version      BIGINT                                 NOT NULL DEFAULT 0,
  del          BOOLEAN DEFAULT FALSE                  NOT NULL
);

CREATE SEQUENCE glvoucher_glvoucherid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE glvoucher_glvoucherid_seq OWNED BY glvoucher.glvoucherid;

CREATE TABLE IF NOT EXISTS glvoucheritem (
  glvoucherid     BIGINT                NOT NULL,
  voucherid       BIGINT                NOT NULL,
  version         BIGINT                NOT NULL DEFAULT 0,
  del             BOOLEAN DEFAULT FALSE NOT NULL,
  glvoucheritemid BIGINT                NOT NULL
);


CREATE SEQUENCE glvoucheritem_glvoucheritemid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE glvoucheritem_glvoucheritemid_seq OWNED BY glvoucheritem.glvoucheritemid;


CREATE TABLE IF NOT EXISTS location (
  locationid                      BIGINT                 NOT NULL,
  title                           CHARACTER VARYING(250) NOT NULL,
  code                            CHARACTER VARYING(40)  NOT NULL,
  parentid                        BIGINT,
  type                            INTEGER                NOT NULL,
  ministryoffinancecode           CHARACTER VARYING(50)  NOT NULL,
  ministryoffinancecodeoftownship CHARACTER VARYING(50)  NOT NULL,
  version                         BIGINT                 NOT NULL DEFAULT 0,
  del                             BOOLEAN DEFAULT FALSE  NOT NULL
);


CREATE SEQUENCE location_locationid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE location_locationid_seq OWNED BY location.locationid;


CREATE TABLE IF NOT EXISTS locationtype (
  locationtypeid INTEGER                NOT NULL,
  title          CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE locationtype_locationtypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE locationtype_locationtypeid_seq OWNED BY locationtype.locationtypeid;


CREATE TABLE IF NOT EXISTS openingoperation (
  openingoperationid BIGINT                                 NOT NULL,
  "Date"             TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  accountid          BIGINT                                 NOT NULL,
  voucherid          BIGINT                                 NOT NULL,
  description        CHARACTER VARYING(250),
  version            BIGINT                                 NOT NULL DEFAULT 0,
  del                BOOLEAN DEFAULT FALSE                  NOT NULL
);


CREATE SEQUENCE openingoperation_openingoperationid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE openingoperation_openingoperationid_seq OWNED BY openingoperation.openingoperationid;


CREATE TABLE IF NOT EXISTS openingoperationitem (
  openingoperationitemid BIGINT                 NOT NULL,
  openingoperationid     BIGINT                 NOT NULL,
  recordtype             CHARACTER VARYING(400) NOT NULL,
  recordid               BIGINT                 NOT NULL,
  checked                BOOLEAN,
  version                BIGINT                 NOT NULL DEFAULT 0,
  del                    BOOLEAN DEFAULT FALSE  NOT NULL
);

CREATE SEQUENCE openingoperationitem_openingoperationitemid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE openingoperationitem_openingoperationitemid_seq OWNED BY openingoperationitem.openingoperationitemid;

CREATE TABLE IF NOT EXISTS party (
  partyid            BIGINT                 NOT NULL,
  type               INTEGER                NOT NULL,
  subtype            INTEGER                NOT NULL,
  name               CHARACTER VARYING(250) NOT NULL,
  lastname           CHARACTER VARYING(250),
  nameen             CHARACTER VARYING(250),
  lastnameen         CHARACTER VARYING(250),
  economiccode       CHARACTER VARYING(50),
  identificationcode CHARACTER VARYING(50),
  website            CHARACTER VARYING(250),
  email              CHARACTER VARYING(250),
  dlid               BIGINT                 NOT NULL,
  isinblacklist      BOOLEAN                NOT NULL,
  avatar             BYTEA,
  version            BIGINT                 NOT NULL DEFAULT 0,
  del                BOOLEAN DEFAULT FALSE  NOT NULL
);


CREATE SEQUENCE party_partyid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE party_partyid_seq OWNED BY party.partyid;


CREATE TABLE IF NOT EXISTS partysubtype (
  partysubtypeid INTEGER                NOT NULL,
  title          CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE partysubtype_partysubtype_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE partysubtype_partysubtype_seq OWNED BY partysubtype.partysubtypeid;

CREATE TABLE IF NOT EXISTS partytype (
  partytypeid INTEGER                NOT NULL,
  title       CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE partytype_partytypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE partytype_partytypeid_seq OWNED BY partytype.partytypeid;

CREATE TABLE IF NOT EXISTS tables (
  tableid BIGINT                 NOT NULL,
  name    CHARACTER VARYING(255) NOT NULL
);

CREATE SEQUENCE tables_tableid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE tables_tableid_seq OWNED BY tables.tableid;

CREATE TABLE IF NOT EXISTS topic (
  topicid    BIGINT                 NOT NULL,
  title      CHARACTER VARYING(250) NOT NULL,
  categoryid BIGINT                 NOT NULL
);


CREATE SEQUENCE topic_topicid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE topic_topicid_seq OWNED BY topic.topicid;


CREATE TABLE IF NOT EXISTS version (
  tableid       BIGINT                                 NOT NULL,
  rowid         BIGINT                                 NOT NULL,
  version       BIGINT                                 NOT NULL DEFAULT 0,
  userid        BIGINT                                 NOT NULL,
  submitdate    TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  description   CHARACTER VARYING(1024),
  rowdata       "_extensions".hstore,
  changedfields "_extensions".hstore,
  equery        TEXT,
  action        TEXT
);

CREATE TABLE IF NOT EXISTS voucher (
  voucherid       BIGINT                                 NOT NULL,
  number          INTEGER                                NOT NULL,
  "Date"          TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  referencenumber INTEGER                                NOT NULL,
  secondarynumber INTEGER,
  state           INTEGER                                NOT NULL,
  type            INTEGER                                NOT NULL,
  fiscalyearid    BIGINT                                 NOT NULL,
  description     CHARACTER VARYING(250),
  dailynumber     INTEGER                                NOT NULL,
  issuersystem    BIGINT                                          DEFAULT -1,
  version         BIGINT                                 NOT NULL DEFAULT 0,
  del             BOOLEAN DEFAULT FALSE                  NOT NULL
);

CREATE SEQUENCE voucher_voucherid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE voucher_voucherid_seq OWNED BY voucher.voucherid;

CREATE TABLE IF NOT EXISTS voucheritem (
  voucheritemid  BIGINT                NOT NULL,
  voucherid      BIGINT                NOT NULL,
  rownumber      INTEGER               NOT NULL,
  accountid      BIGINT                NOT NULL,
  dlid           BIGINT                NOT NULL,
  debit          NUMERIC(19, 4)        NOT NULL,
  credit         NUMERIC(19, 4)        NOT NULL,
  currencyid     BIGINT                NOT NULL,
  currencyrate   NUMERIC(26, 16),
  currencydebit  NUMERIC(19, 4),
  currencycredit NUMERIC(19, 4),
  trackingnumber CHARACTER VARYING(40),
  trackingdate   TIMESTAMP WITH TIME ZONE,
  description    CHARACTER VARYING(250),
  version        BIGINT                NOT NULL DEFAULT 0,
  del            BOOLEAN DEFAULT FALSE NOT NULL
);

CREATE SEQUENCE voucheritem_voucheritemid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;


ALTER SEQUENCE voucheritem_voucheritemid_seq OWNED BY voucheritem.voucheritemid;


CREATE TABLE IF NOT EXISTS vouchertype (
  vouchertypeid INTEGER                NOT NULL,
  title         CHARACTER VARYING(250) NOT NULL
);

CREATE SEQUENCE vouchertype_vouchertypeid_seq
START WITH 1
INCREMENT BY 1
NO MINVALUE
NO MAXVALUE
CACHE 1;

ALTER SEQUENCE vouchertype_vouchertypeid_seq OWNED BY vouchertype.vouchertypeid;


ALTER TABLE ONLY account
  ALTER COLUMN accountid SET DEFAULT nextval('account_accountid_seq' :: REGCLASS);

ALTER TABLE ONLY accountbalancetype
  ALTER COLUMN accountbalancetypeid SET DEFAULT nextval('accountbalancetype_accountbalancetypeid_seq' :: REGCLASS);

ALTER TABLE ONLY bank
  ALTER COLUMN bankid SET DEFAULT nextval('bank_bankid_seq' :: REGCLASS);

ALTER TABLE ONLY bankaccount
  ALTER COLUMN bankaccountid SET DEFAULT nextval('bankaccount_bankaccountid_seq' :: REGCLASS);

ALTER TABLE ONLY bankaccounttype
  ALTER COLUMN bankaccounttypeid SET DEFAULT nextval('bankaccounttype_bankaccounttypeid_seq' :: REGCLASS);

ALTER TABLE ONLY bankbranch
  ALTER COLUMN bankbranchid SET DEFAULT nextval('bankbranch_bankbranchid_seq' :: REGCLASS);

ALTER TABLE ONLY cash
  ALTER COLUMN cashid SET DEFAULT nextval('cash_cashid_seq' :: REGCLASS);

ALTER TABLE ONLY category
  ALTER COLUMN categoryid SET DEFAULT nextval('category_categoryid_seq' :: REGCLASS);

ALTER TABLE ONLY categorytype
  ALTER COLUMN categorytypeid SET DEFAULT nextval('categorytype_categorytypeid_seq' :: REGCLASS);

ALTER TABLE ONLY config
  ALTER COLUMN configid SET DEFAULT nextval('config_configid_seq' :: REGCLASS);

ALTER TABLE ONLY costcenter
  ALTER COLUMN costcenterid SET DEFAULT nextval('costcenter_costcenterid_seq' :: REGCLASS);

ALTER TABLE ONLY costcentertype
  ALTER COLUMN costcentertypeid SET DEFAULT nextval('costcentertype_costcentertypeid_seq' :: REGCLASS);

ALTER TABLE ONLY currency
  ALTER COLUMN currencyid SET DEFAULT nextval('currency_currencyid_seq' :: REGCLASS);

ALTER TABLE ONLY currencyexchangerate
  ALTER COLUMN currencyexchangerateid SET DEFAULT nextval(
    'currencyexchangerate_currencyexchangerateid_seq' :: REGCLASS);

ALTER TABLE ONLY dl
  ALTER COLUMN dlid SET DEFAULT nextval('dl_dlid_seq' :: REGCLASS);

ALTER TABLE ONLY dltype
  ALTER COLUMN dltypeid SET DEFAULT nextval('dltype_dltypeid_seq' :: REGCLASS);

ALTER TABLE ONLY fiscalyear
  ALTER COLUMN fiscalyearid SET DEFAULT nextval('fiscalyear_fiscalyearid_seq' :: REGCLASS);

ALTER TABLE ONLY glvoucher
  ALTER COLUMN glvoucherid SET DEFAULT nextval('glvoucher_glvoucherid_seq' :: REGCLASS);

ALTER TABLE ONLY glvoucheritem
  ALTER COLUMN glvoucheritemid SET DEFAULT nextval('glvoucheritem_glvoucheritemid_seq' :: REGCLASS);

ALTER TABLE ONLY location
  ALTER COLUMN locationid SET DEFAULT nextval('location_locationid_seq' :: REGCLASS);

ALTER TABLE ONLY locationtype
  ALTER COLUMN locationtypeid SET DEFAULT nextval('locationtype_locationtypeid_seq' :: REGCLASS);

ALTER TABLE ONLY openingoperation
  ALTER COLUMN openingoperationid SET DEFAULT nextval('openingoperation_openingoperationid_seq' :: REGCLASS);

ALTER TABLE ONLY openingoperationitem
  ALTER COLUMN openingoperationitemid SET DEFAULT nextval(
    'openingoperationitem_openingoperationitemid_seq' :: REGCLASS);

ALTER TABLE ONLY party
  ALTER COLUMN partyid SET DEFAULT nextval('party_partyid_seq' :: REGCLASS);

ALTER TABLE ONLY partysubtype
  ALTER COLUMN partysubtypeid SET DEFAULT nextval('partysubtype_partysubtype_seq' :: REGCLASS);

ALTER TABLE ONLY partytype
  ALTER COLUMN partytypeid SET DEFAULT nextval('partytype_partytypeid_seq' :: REGCLASS);

ALTER TABLE ONLY tables
  ALTER COLUMN tableid SET DEFAULT nextval('tables_tableid_seq' :: REGCLASS);

ALTER TABLE ONLY topic
  ALTER COLUMN topicid SET DEFAULT nextval('topic_topicid_seq' :: REGCLASS);

ALTER TABLE ONLY voucher
  ALTER COLUMN voucherid SET DEFAULT nextval('voucher_voucherid_seq' :: REGCLASS);

ALTER TABLE ONLY voucheritem
  ALTER COLUMN voucheritemid SET DEFAULT nextval('voucheritem_voucheritemid_seq' :: REGCLASS);

ALTER TABLE ONLY vouchertype
  ALTER COLUMN vouchertypeid SET DEFAULT nextval('vouchertype_vouchertypeid_seq' :: REGCLASS);


SELECT pg_catalog.setval('account_accountid_seq', 1, FALSE);

SELECT pg_catalog.setval('accountbalancetype_accountbalancetypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('bank_bankid_seq', 1, TRUE);

SELECT pg_catalog.setval('bankaccount_bankaccountid_seq', 1, FALSE);

SELECT pg_catalog.setval('bankaccounttype_bankaccounttypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('bankbranch_bankbranchid_seq', 1, FALSE);

SELECT pg_catalog.setval('cash_cashid_seq', 1, FALSE);

SELECT pg_catalog.setval('category_categoryid_seq', 1, FALSE);

SELECT pg_catalog.setval('categorytype_categorytypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('config_configid_seq', 1000, TRUE);

SELECT pg_catalog.setval('costcenter_costcenterid_seq', 1, FALSE);

SELECT pg_catalog.setval('costcentertype_costcentertypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('currency_currencyid_seq', 1, FALSE);

SELECT pg_catalog.setval('currencyexchangerate_currencyexchangerateid_seq', 1, FALSE);

SELECT pg_catalog.setval('dl_dlid_seq', 1, FALSE);

SELECT pg_catalog.setval('dltype_dltypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('fiscalyear_fiscalyearid_seq', 4, TRUE);

SELECT pg_catalog.setval('glvoucher_glvoucherid_seq', 1, FALSE);

SELECT pg_catalog.setval('glvoucheritem_glvoucheritemid_seq', 1, FALSE);

SELECT pg_catalog.setval('location_locationid_seq', 1, FALSE);

SELECT pg_catalog.setval('locationtype_locationtypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('openingoperation_openingoperationid_seq', 1, FALSE);

SELECT pg_catalog.setval('openingoperationitem_openingoperationitemid_seq', 1, FALSE);

SELECT pg_catalog.setval('party_partyid_seq', 1, FALSE);

SELECT pg_catalog.setval('partysubtype_partysubtype_seq', 1, FALSE);

SELECT pg_catalog.setval('partytype_partytypeid_seq', 1, FALSE);

SELECT pg_catalog.setval('tables_tableid_seq', 1, FALSE);

SELECT pg_catalog.setval('topic_topicid_seq', 1, FALSE);

SELECT pg_catalog.setval('voucher_voucherid_seq', 1, FALSE);

SELECT pg_catalog.setval('voucheritem_voucheritemid_seq', 1, FALSE);

SELECT pg_catalog.setval('vouchertype_vouchertypeid_seq', 1, FALSE);


ALTER TABLE ONLY account
  ADD CONSTRAINT account_pkey PRIMARY KEY (accountid);

ALTER TABLE ONLY account
  ADD CONSTRAINT account_version_key UNIQUE (version);

ALTER TABLE ONLY accountbalancetype
  ADD CONSTRAINT accountbalancetype_pkey PRIMARY KEY (accountbalancetypeid);

ALTER TABLE ONLY accounttopic
  ADD CONSTRAINT accounttopic_pkey PRIMARY KEY (topicid, accountid);

ALTER TABLE ONLY bank
  ADD CONSTRAINT bank_pkey PRIMARY KEY (bankid);

ALTER TABLE ONLY bankaccount
  ADD CONSTRAINT bankaccount_pkey PRIMARY KEY (bankaccountid);

ALTER TABLE ONLY bankaccounttype
  ADD CONSTRAINT bankaccounttype_pkey PRIMARY KEY (bankaccounttypeid);

ALTER TABLE ONLY bankbranch
  ADD CONSTRAINT bankbranch_pkey PRIMARY KEY (bankbranchid);

ALTER TABLE ONLY cash
  ADD CONSTRAINT cash_pkey PRIMARY KEY (cashid);

ALTER TABLE ONLY category
  ADD CONSTRAINT category_pkey PRIMARY KEY (categoryid);

ALTER TABLE ONLY categorytype
  ADD CONSTRAINT categorytype_pkey PRIMARY KEY (categorytypeid);

ALTER TABLE ONLY config
  ADD CONSTRAINT config_configid_pk PRIMARY KEY (configid);

ALTER TABLE ONLY costcenter
  ADD CONSTRAINT costcenter_pkey PRIMARY KEY (costcenterid);

ALTER TABLE ONLY costcentertype
  ADD CONSTRAINT costcentertype_pkey PRIMARY KEY (costcentertypeid);

ALTER TABLE ONLY currency
  ADD CONSTRAINT currency_pkey PRIMARY KEY (currencyid);

ALTER TABLE ONLY currencyexchangerate
  ADD CONSTRAINT currencyexchangerate_pkey PRIMARY KEY (currencyexchangerateid);

ALTER TABLE ONLY dl
  ADD CONSTRAINT dl_pkey PRIMARY KEY (dlid);

ALTER TABLE ONLY dltype
  ADD CONSTRAINT dltype_pkey PRIMARY KEY (dltypeid);

ALTER TABLE ONLY fiscalyear
  ADD CONSTRAINT fiscalyear_pkey PRIMARY KEY (fiscalyearid);

ALTER TABLE ONLY glvoucher
  ADD CONSTRAINT glvoucher_pkey PRIMARY KEY (glvoucherid);

ALTER TABLE ONLY glvoucheritem
  ADD CONSTRAINT glvoucheritem_glvoucheritemid_pk PRIMARY KEY (glvoucheritemid);

ALTER TABLE ONLY location
  ADD CONSTRAINT location_pkey PRIMARY KEY (locationid);

ALTER TABLE ONLY locationtype
  ADD CONSTRAINT locationtype_pkey PRIMARY KEY (locationtypeid);

ALTER TABLE ONLY openingoperation
  ADD CONSTRAINT openingoperation_pkey PRIMARY KEY (openingoperationid);

ALTER TABLE ONLY openingoperationitem
  ADD CONSTRAINT openingoperationitem_pkey PRIMARY KEY (openingoperationitemid);

ALTER TABLE ONLY party
  ADD CONSTRAINT party_pkey PRIMARY KEY (partyid);

ALTER TABLE ONLY partysubtype
  ADD CONSTRAINT partysubtype_pkey PRIMARY KEY (partysubtypeid);

ALTER TABLE ONLY partytype
  ADD CONSTRAINT partytype_pkey PRIMARY KEY (partytypeid);

ALTER TABLE ONLY tables
  ADD CONSTRAINT tables_pkey PRIMARY KEY (tableid);

ALTER TABLE ONLY topic
  ADD CONSTRAINT topic_pkey PRIMARY KEY (topicid);

ALTER TABLE ONLY version
  ADD CONSTRAINT version_pkey PRIMARY KEY (tableid, rowid, version);

ALTER TABLE ONLY voucher
  ADD CONSTRAINT voucher_pkey PRIMARY KEY (voucherid);

ALTER TABLE ONLY voucheritem
  ADD CONSTRAINT voucheritem_pkey PRIMARY KEY (voucheritemid);

ALTER TABLE ONLY vouchertype
  ADD CONSTRAINT vouchertype_pkey PRIMARY KEY (vouchertypeid);

CREATE UNIQUE INDEX account_code ON account USING BTREE (code);

CREATE UNIQUE INDEX dl_code ON dl USING BTREE (code);

ALTER TABLE ONLY account
  ADD CONSTRAINT fkaccount464978 FOREIGN KEY (balancetype) REFERENCES accountbalancetype (accountbalancetypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY account
  ADD CONSTRAINT fkaccount555592 FOREIGN KEY (parentid) REFERENCES account (accountid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY accounttopic
  ADD CONSTRAINT fkaccounttop657317 FOREIGN KEY (accountid) REFERENCES account (accountid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY accounttopic
  ADD CONSTRAINT fkaccounttop743736 FOREIGN KEY (topicid) REFERENCES topic (topicid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY bankaccount
  ADD CONSTRAINT fkbankaccoun510318 FOREIGN KEY (dlid) REFERENCES dl (dlid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY bankaccount
  ADD CONSTRAINT fkbankaccoun586688 FOREIGN KEY (bankaccounttypeid) REFERENCES bankaccounttype (bankaccounttypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY bankaccount
  ADD CONSTRAINT fkbankaccoun599249 FOREIGN KEY (currencyid) REFERENCES currency (currencyid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY bankaccount
  ADD CONSTRAINT fkbankaccoun731590 FOREIGN KEY (bankbranchid) REFERENCES bankbranch (bankbranchid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY bankbranch
  ADD CONSTRAINT fkbankbranch684888 FOREIGN KEY (bankid) REFERENCES bank (bankid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY bankbranch
  ADD CONSTRAINT fkbankbranch970953 FOREIGN KEY (locationid) REFERENCES location (locationid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY cash
  ADD CONSTRAINT fkcash297383 FOREIGN KEY (dlid) REFERENCES dl (dlid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY cash
  ADD CONSTRAINT fkcash812184 FOREIGN KEY (currencyid) REFERENCES currency (currencyid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY category
  ADD CONSTRAINT fkcategory276962 FOREIGN KEY (type) REFERENCES categorytype (categorytypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY costcenter
  ADD CONSTRAINT fkcostcenter478444 FOREIGN KEY (dlid) REFERENCES dl (dlid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY costcenter
  ADD CONSTRAINT fkcostcenter779458 FOREIGN KEY (type) REFERENCES costcentertype (costcentertypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY currencyexchangerate
  ADD CONSTRAINT fkcurrencyex54543 FOREIGN KEY (fiscalyearid) REFERENCES fiscalyear (fiscalyearid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY currencyexchangerate
  ADD CONSTRAINT fkcurrencyex68234 FOREIGN KEY (currencyid) REFERENCES currency (currencyid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY dl
  ADD CONSTRAINT fkdl70390 FOREIGN KEY (type) REFERENCES dltype (dltypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY glvoucher
  ADD CONSTRAINT fkglvoucher692499 FOREIGN KEY (fiscalyearid) REFERENCES fiscalyear (fiscalyearid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY glvoucheritem
  ADD CONSTRAINT fkglvoucheri2846 FOREIGN KEY (glvoucherid) REFERENCES glvoucher (glvoucherid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY glvoucheritem
  ADD CONSTRAINT fkglvoucheri957496 FOREIGN KEY (voucherid) REFERENCES voucher (voucherid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY location
  ADD CONSTRAINT fklocation24558 FOREIGN KEY (type) REFERENCES locationtype (locationtypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY openingoperationitem
  ADD CONSTRAINT fkopeningope268300 FOREIGN KEY (openingoperationid) REFERENCES openingoperation (openingoperationid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY openingoperation
  ADD CONSTRAINT fkopeningope300419 FOREIGN KEY (accountid) REFERENCES account (accountid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY openingoperation
  ADD CONSTRAINT fkopeningope948549 FOREIGN KEY (voucherid) REFERENCES voucher (voucherid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY party
  ADD CONSTRAINT fkparty274801 FOREIGN KEY (subtype) REFERENCES partysubtype (partysubtypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY party
  ADD CONSTRAINT fkparty675290 FOREIGN KEY (type) REFERENCES partytype (partytypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY party
  ADD CONSTRAINT fkparty89253 FOREIGN KEY (dlid) REFERENCES dl (dlid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY topic
  ADD CONSTRAINT fktopic795702 FOREIGN KEY (categoryid) REFERENCES category (categoryid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY version
  ADD CONSTRAINT fkversion246025 FOREIGN KEY (tableid) REFERENCES tables (tableid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY voucher
  ADD CONSTRAINT fkvoucher87077 FOREIGN KEY (type) REFERENCES vouchertype (vouchertypeid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY voucher
  ADD CONSTRAINT fkvoucher956379 FOREIGN KEY (fiscalyearid) REFERENCES fiscalyear (fiscalyearid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY voucheritem
  ADD CONSTRAINT fkvoucherite22053 FOREIGN KEY (dlid) REFERENCES dl (dlid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY voucheritem
  ADD CONSTRAINT fkvoucherite28729 FOREIGN KEY (accountid) REFERENCES account (accountid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY voucheritem
  ADD CONSTRAINT fkvoucherite380598 FOREIGN KEY (voucherid) REFERENCES voucher (voucherid) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ONLY voucheritem
  ADD CONSTRAINT fkvoucherite87515 FOREIGN KEY (currencyid) REFERENCES currency (currencyid) ON UPDATE CASCADE ON DELETE RESTRICT;


/* Version log Trigger */
CREATE OR REPLACE FUNCTION versionTrigger()
  RETURNS TRIGGER AS $body$
DECLARE
  audit_row "AccountingRelay".version;
  h_old     "_extensions".hstore;
  rid       BIGINT;
  uid       BIGINT;
  udesc     TEXT;
BEGIN
  IF TG_WHEN <> 'AFTER'
  THEN
    RAISE EXCEPTION 'versionTrigger() may only run as an AFTER trigger';
  END IF;

  EXECUTE format('SELECT ($1).%I::BIGINT', TG_ARGV [1])
  USING NEW
  INTO  rid;

  SELECT
    cuser.uid,
    cuser.desc
  INTO uid, udesc
  FROM cuser;

  audit_row = ROW (
              TG_ARGV [0] :: INT, -- Table ID
              rid, -- Row ID
              0, -- Version
              uid, -- user id
              statement_timestamp(), -- submit time
              udesc, -- description
              NULL, NULL, -- row_data, changed_fields
              current_query(), -- top-level query or queries (if multistatement) from client
              substring(TG_OP, 1, 1)                          -- action
  );


  IF (TG_OP = 'UPDATE' AND TG_LEVEL = 'ROW')
  THEN
    audit_row.rowdata = "_extensions".hstore(OLD.*);
    audit_row.changedfields = ("_extensions".hstore(NEW.*) - audit_row.rowdata);
    audit_row.version = OLD.version + 1;

    IF (audit_row.changed_fields = "_extensions".hstore('')) OR
       ((array_length(akeys(audit_row.changedfields), 1) = 1) AND (audit_row.changedfields ? 'version'))
    THEN
      RETURN NULL;
    END IF;
    EXECUTE format('UPDATE %I SET version=%s WHERE %I=%L;', TG_TABLE_NAME, audit_row.version, TG_ARGV [1], rid);
  ELSIF (TG_OP = 'DELETE' AND TG_LEVEL = 'ROW')
    THEN
      audit_row.rowdata = "_extensions".hstore(OLD.*);
      audit_row.version = OLD.version + 1;
  ELSIF (TG_OP = 'INSERT' AND TG_LEVEL = 'ROW')
    THEN
      audit_row.rowdata = "_extensions".hstore(NEW.*);
  ELSE
    RAISE EXCEPTION '[versionTrigger] - Trigger func added as trigger for unhandled case: %, %', TG_OP, TG_LEVEL;
    RETURN NULL;
  END IF;
  INSERT INTO "AccountingRelay".version VALUES (audit_row.*);
  RETURN NULL;
END;
$body$
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = pg_catalog, public;

/* store data for version trigger */
CREATE OR REPLACE FUNCTION versionData(userid BIGINT, opdescription TEXT)
  RETURNS VOID AS $body$
DECLARE
BEGIN
  CREATE TEMP TABLE IF NOT EXISTS cuser (
    uid    BIGINT,
    "desc" TEXT
  );
  DELETE FROM cuser;
  INSERT INTO cuser VALUES (userid, opdescription);
END;
$body$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION enableVersioning(target_table REGCLASS, tableid BIGINT, keyfield TEXT)
  RETURNS VOID AS $body$
DECLARE
  stm_targets TEXT = 'INSERT OR UPDATE OR DELETE';
  _q_txt      TEXT;
BEGIN
  EXECUTE 'DROP TRIGGER IF EXISTS versionlogger ON ' || quote_ident(target_table :: TEXT);

  _q_txt = 'CREATE TRIGGER versionlogger AFTER INSERT OR UPDATE OR DELETE ON ' ||
           quote_ident(target_table :: TEXT) ||
           ' FOR EACH ROW EXECUTE PROCEDURE versionTrigger(' ||
           tableid || ',' || keyfield || ');';
  RAISE NOTICE '%', _q_txt;
  EXECUTE _q_txt;


END;
$body$
LANGUAGE 'plpgsql';


INSERT INTO tables SELECT
                     1,
                     'account';
SELECT enableVersioning('account', 1, 'accountid');
INSERT INTO tables SELECT
                     2,
                     'accountbalancetype';
INSERT INTO tables SELECT
                     3,
                     'accounttopic';
INSERT INTO tables SELECT
                     4,
                     'bank';
SELECT enableVersioning('bank', 4, 'bankid');
INSERT INTO tables SELECT
                     5,
                     'bankaccount';
SELECT enableVersioning('bankaccount', 5, 'bankaccountid');
INSERT INTO tables SELECT
                     6,
                     'bankaccounttype';
SELECT enableVersioning('bankaccounttype', 6, 'bankaccounttypeid');
INSERT INTO tables SELECT
                     7,
                     'bankbranch';
SELECT enableVersioning('bankbranch', 7, 'bankbranchid');
INSERT INTO tables SELECT
                     8,
                     'cash';
SELECT enableVersioning('cash', 8, 'cashid');
INSERT INTO tables SELECT
                     9,
                     'category';
INSERT INTO tables SELECT
                     10,
                     'categorytype';
INSERT INTO tables SELECT
                     11,
                     'config';
SELECT enableVersioning('config', 11, 'configid');
INSERT INTO tables SELECT
                     12,
                     'costcenter';
SELECT enableVersioning('costcenter', 12, 'costcenterid');
INSERT INTO tables SELECT
                     13,
                     'costcentertype';
INSERT INTO tables SELECT
                     14,
                     'currency';
SELECT enableVersioning('currency', 14, 'currencyid');
INSERT INTO tables SELECT
                     15,
                     'currencyexchangerate';
SELECT enableVersioning('currencyexchangerate', 15, 'currencyexchangerateid');
INSERT INTO tables SELECT
                     16,
                     'dl';
SELECT enableVersioning('dl', 16, 'dlid');
INSERT INTO tables SELECT
                     17,
                     'dltype';
INSERT INTO tables SELECT
                     18,
                     'fiscalyear';
SELECT enableVersioning('fiscalyear', 18, 'fiscalyearid');
INSERT INTO tables SELECT
                     19,
                     'glvoucher';
SELECT enableVersioning('glvoucher', 19, 'glvoucherid');
INSERT INTO tables SELECT
                     20,
                     'glvoucheritem';
SELECT enableVersioning('glvoucheritem', 20, 'glvoucheritemid');
INSERT INTO tables SELECT
                     21,
                     'location';
SELECT enableVersioning('location', 21, 'locationid');
INSERT INTO tables SELECT
                     22,
                     'locationtype';
INSERT INTO tables SELECT
                     23,
                     'openingoperation';
SELECT enableVersioning('openingoperation', 23, 'openingoperationid');
INSERT INTO tables SELECT
                     24,
                     'openingoperationitem';
SELECT enableVersioning('openingoperationitem', 24, 'openingoperationitemid');
INSERT INTO tables SELECT
                     25,
                     'party';
SELECT enableVersioning('party', 25, 'partyid');
INSERT INTO tables SELECT
                     26,
                     'partysubtype';
INSERT INTO tables SELECT
                     27,
                     'partytype';
INSERT INTO tables SELECT
                     28,
                     'tables';
INSERT INTO tables SELECT
                     29,
                     'topic';
INSERT INTO tables SELECT
                     30,
                     'version';
INSERT INTO tables SELECT
                     31,
                     'voucher';
SELECT enableVersioning('voucher', 31, 'voucherid');
INSERT INTO tables SELECT
                     32,
                     'voucher';
SELECT enableVersioning('voucher', 32, 'voucheritemid');
INSERT INTO tables SELECT
                     33,
                     'vouchertype';
CREATE OR REPLACE FUNCTION setConfig(
  uid    BIGINT,
  iname  TEXT,
  ivalue TEXT
)
  RETURNS VOID AS $$
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE config
  SET "value" = ivalue
  WHERE "name" = iname;
  IF NOT FOUND
  THEN
    INSERT INTO config VALUES (iname, ivalue, 0);
  END IF;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION getConfig(
  uid   BIGINT,
  iname TEXT
)
  RETURNS TEXT AS $$
DECLARE retval TEXT;
BEGIN
  PERFORM versiondata(uid, '');
  SELECT "value"
  FROM config
  WHERE name = iname
  INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

SELECT setconfig(-1, 'codeCLlen', '2');
SELECT setconfig(-1, 'codeGLlen', '2');
SELECT setconfig(-1, 'codeSLlen', '3');
SELECT setconfig(-1, 'codeDLlen', '4');
CREATE OR REPLACE FUNCTION newFiscalYear(
  uid    BIGINT,
  ititle TEXT,
  istart DATE,
  iend   DATE
)
  RETURNS BIGINT AS $$
DECLARE
  retval BIGINT;
  tempv  BIGINT;
BEGIN
  PERFORM versiondata(uid, '');
  SELECT count(*)
  FROM fiscalyear
  WHERE status = 1
  INTO tempv;
  IF tempv > 0
  THEN
    RAISE EXCEPTION 'Close active fiscal year first';
  END IF;
  INSERT INTO fiscalyear (title, startdate, enddate, status, VERSION)
  VALUES (ititle, istart, iend, 1, 0)
  RETURNING fiscalyearid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION closeFiscalYear(
  uid BIGINT,
  id  BIGINT
)
  RETURNS VOID AS $$
DECLARE
  retval BIGINT;
  tempv  BIGINT;
BEGIN
  PERFORM versiondata(uid, '');
  SELECT status
  FROM fiscalyear
  WHERE fiscalyearid = id
  INTO tempv;
  IF tempv IS NULL
  THEN
    RAISE EXCEPTION 'Invalid fiscal year id';
  END IF;
  IF tempv = 2
  THEN
    RAISE EXCEPTION 'This fiscal year is closed already';
  END IF;
  SELECT count(*)
  FROM voucher
  WHERE state = 1 AND voucher.fiscalyearid = id
  INTO tempv;
  IF tempv > 0
  THEN
    RAISE EXCEPTION 'All vouchers are not finalized';
  END IF;

  UPDATE fiscalyear
  SET status = 2;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION newAccount(
  uid                    BIGINT,
  iparent                BIGINT,
  itype                  INTEGER,
  icode                  VARCHAR(40),
  ititle                 VARCHAR(250),
  ititle2                VARCHAR(250),
  iisactive              BOOLEAN,
  icashflowcategory      INTEGER,
  iopeningbalance        NUMERIC(19, 4),
  ibalancetype           INTEGER,
  ihasbaancetypecheck    BOOLEAN,
  ihasdl                 BOOLEAN,
  ihascurrency           BOOLEAN,
  ihascurrencyconversion BOOLEAN,
  ihastracking           BOOLEAN,
  ihastrackingcheck      BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO account
  VALUES (DEFAULT, iparent, itype, icode, ititle, ititle2, iisactive, icashflowcategory, iopeningbalance, ibalancetype,
                   ihasbaancetypecheck, ihasdl, ihascurrency, ihascurrencyconversion, ihastracking, ihastrackingcheck
  )
  RETURNING accountid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyAccount(
  uid                    BIGINT,
  iid                    BIGINT,
  iparent                BIGINT,
  itype                  INTEGER,
  icode                  VARCHAR(40),
  ititle                 VARCHAR(250),
  ititle2                VARCHAR(250),
  iisactive              BOOLEAN,
  icashflowcategory      INTEGER,
  ibalancetype           INTEGER,
  ihasbaancetypecheck    BOOLEAN,
  ihasdl                 BOOLEAN,
  ihascurrency           BOOLEAN,
  ihascurrencyconversion BOOLEAN,
  ihastracking           BOOLEAN,
  ihastrackingcheck      BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE account
  SET
    parentid    = iparent, balancetype = ibalancetype, type = itype, code = icode, title = ititle, title2 = ititle2,
    isactive    = iisactive, cashflowcategory = icashflowcategory, hasbalancetypecheck = ihasbaancetypecheck,
    hasdl       = ihasdl, hascurrency = ihascurrency, hascurrencyconversion = ihascurrencyconversion,
    hastracking = ihastracking, hastrackingcheck = ihastrackingcheck
  WHERE accountid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeAccount(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE account
  SET
    del = TRUE
  WHERE accountid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newDL(
  uid       BIGINT,
  itype     INTEGER,
  icode     VARCHAR(40),
  ititle    VARCHAR(250),
  ititle2   VARCHAR(250),
  iisactive BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO dl
  VALUES (DEFAULT, icode, ititle, ititle2, itype, iisactive
  )
  RETURNING dlid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyDL(
  uid       BIGINT,
  iid       BIGINT,
  itype     INTEGER,
  icode     VARCHAR(40),
  ititle    VARCHAR(250),
  ititle2   VARCHAR(250),
  iisactive BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE dl
  SET
    type = itype, code = icode, title = ititle, title2 = ititle2, isactive = iisactive
  WHERE dlid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeDL(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE dl
  SET
    del = TRUE
  WHERE dlid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION activeDL(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE dl
  SET
    isactive = TRUE
  WHERE dlid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION deactivateDL(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE dl
  SET
    isactive = FALSE
  WHERE dlid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newCategory(
  uid    BIGINT,
  itype  INTEGER,
  ititle VARCHAR(250)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO category
  VALUES (DEFAULT, itype, ititle
  )
  RETURNING categoryid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyCategory(
  uid    BIGINT,
  iid    BIGINT,
  itype  INTEGER,
  ititle VARCHAR(250)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE category
  SET
    type = itype, title = ititle
  WHERE categoryid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeCategory(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  DELETE FROM category
  WHERE categoryid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newTopic(
  uid       BIGINT,
  icategory BIGINT,
  ititle    VARCHAR(250)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO topic
  VALUES (DEFAULT, ititle, icategory
  )
  RETURNING topicid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyTopic(
  uid       BIGINT,
  iid       BIGINT,
  icategory BIGINT,
  ititle    VARCHAR(250)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE topic
  SET
    categoryid = icategory, title = ititle
  WHERE topicid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeTopic(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  DELETE FROM topic
  WHERE topicid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION addAccountTopic(
  uid      BIGINT,
  iaccount BIGINT,
  itopic   BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO accounttopic
  VALUES (itopic, iaccount
  );
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeAccountTopic(
  uid      BIGINT,
  iaccount BIGINT,
  itopic   BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  DELETE FROM accounttopic
  WHERE topicid = itopic AND accountid = iaccount;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION newVoucher(
  uid              BIGINT,
  inumber          INTEGER,
  ireferencenumber INTEGER,
  isecondarynumber INTEGER,
  idailynumber     INTEGER,
  iDate            TIMESTAMP WITH TIME ZONE,
  itype            INTEGER,
  idescription     CHARACTER VARYING(250),
  ifiscalyearid    BIGINT,
  istate           INTEGER
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO voucher
  VALUES (DEFAULT, inumber, iDate, ireferencenumber, isecondarynumber, istate, itype, ifiscalyearid, idescription,
          idailynumber)
  RETURNING voucherid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyVoucher(
  uid              BIGINT,
  iid              BIGINT,
  inumber          INTEGER,
  ireferencenumber INTEGER,
  isecondarynumber INTEGER,
  idailynumber     INTEGER,
  iDate            TIMESTAMP WITH TIME ZONE,
  itype            INTEGER,
  idescription     CHARACTER VARYING(250),
  ifiscalyearid    BIGINT,
  istate           INTEGER
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucher
  SET
    number      = inumber, "Date" = iDate, referencenumber = ireferencenumber, secondarynumber = isecondarynumber,
    state       = istate, "type" = itype, fiscalyearid = ifiscalyearid, description = idescription,
    dailynumber = idailynumber
  WHERE voucherid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeVoucher(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucher
  SET
    del = TRUE
  WHERE voucherid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION finalizeVoucher(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucher
  SET
    state = 2
  WHERE voucherid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newVoucherItem(
  uid             BIGINT,
  ivoucherid      BIGINT,
  irownumber      INTEGER, iaccountid BIGINT, idlid BIGINT, idebit NUMERIC(19, 4), icredit NUMERIC(19, 4),
  icurrencyid     BIGINT, icurrencyrate NUMERIC(26, 16), icurrencydebit NUMERIC(19, 4), icurrencycredit NUMERIC(19, 4),
  itrackingnumber VARCHAR(40), itrackingdate TIMESTAMPTZ, idescription VARCHAR(250)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO voucheritem
  VALUES
    (DEFAULT, ivoucherid, irownumber, iaccountid, idlid, idebit, icredit, icurrencyid, icurrencyrate, icurrencydebit,
              icurrencycredit, itrackingnumber, itrackingdate, idescription)
  RETURNING voucheritemid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyVoucherItem(
  uid             BIGINT,
  iid             BIGINT,
  ivoucherid      BIGINT,
  irownumber      INTEGER, iaccountid BIGINT, idlid BIGINT, idebit NUMERIC(19, 4), icredit NUMERIC(19, 4),
  icurrencyid     BIGINT, icurrencyrate NUMERIC(26, 16), icurrencydebit NUMERIC(19, 4), icurrencycredit NUMERIC(19, 4),
  itrackingnumber VARCHAR(40), itrackingdate TIMESTAMPTZ, idescription VARCHAR(250)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucheritem
  SET
    voucherid      = ivoucherid, rownumber = irownumber, accountid = iaccountid, dlid = idlid, debit = idebit,
    credit         = icredit, currencyid = icurrencyid, currencyrate = icurrencyrate, currencydebit = icurrencydebit,
    currencycredit = icurrencycredit, trackingnumber = itrackingnumber, trackingdate = itrackingdate,
    description    = idescription
  WHERE voucheritemid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeVoucherItem(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucheritem
  SET
    del = TRUE
  WHERE voucheritemid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newGLVoucher(
  uid         BIGINT,
  ifiscalyear BIGINT,
  inumber     INTEGER,
  idate       TIMESTAMPTZ
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO glvoucher
  VALUES
    (DEFAULT, ifiscalyear, inumber, idate)
  RETURNING glvoucherid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeGLVoucher(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE glvoucher
  SET
    del = TRUE
  WHERE glvoucherid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newGLVoucherItem(
  uid      BIGINT,
  iglv     BIGINT,
  ivoucher BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO glvoucheritem
  VALUES
    (DEFAULT, iglv, ivoucher)
  RETURNING glvoucheritemid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeGLVoucherItem(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE glvoucheritem
  SET
    del = TRUE
  WHERE glvoucheritemid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION newVoucher(
  uid              BIGINT,
  inumber          INTEGER,
  ireferencenumber INTEGER,
  isecondarynumber INTEGER,
  idailynumber     INTEGER,
  iDate            TIMESTAMP WITH TIME ZONE,
  itype            INTEGER,
  idescription     CHARACTER VARYING(250),
  ifiscalyearid    BIGINT,
  istate           INTEGER
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO voucher
  VALUES (DEFAULT, inumber, iDate, ireferencenumber, isecondarynumber, istate, itype, ifiscalyearid, idescription,
          idailynumber)
  RETURNING voucherid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyVoucher(
  uid              BIGINT,
  iid              BIGINT,
  inumber          INTEGER,
  ireferencenumber INTEGER,
  isecondarynumber INTEGER,
  idailynumber     INTEGER,
  iDate            TIMESTAMP WITH TIME ZONE,
  itype            INTEGER,
  idescription     CHARACTER VARYING(250),
  ifiscalyearid    BIGINT,
  istate           INTEGER
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucher
  SET
    number      = inumber, "Date" = iDate, referencenumber = ireferencenumber, secondarynumber = isecondarynumber,
    state       = istate, "type" = itype, fiscalyearid = ifiscalyearid, description = idescription,
    dailynumber = idailynumber
  WHERE voucherid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeVoucher(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE voucher
  SET
    del = TRUE
  WHERE voucherid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newCash(
  uid          BIGINT,
  ititle       VARCHAR(250),
  iDL          BIGINT,
  icurrency    BIGINT,
  irate        NUMERIC(26, 16),
  ifirstamount NUMERIC(19, 4),
  ifirstdate   TIMESTAMPTZ,
  ibalance     NUMERIC(19, 4)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO cash
  VALUES (DEFAULT, ititle, iDL, icurrency, irate, ifirstamount, ifirstdate, ibalance)
  RETURNING cashid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyCash(
  uid          BIGINT,
  iid          BIGINT,
  ititle       VARCHAR(250),
  iDL          BIGINT,
  icurrency    BIGINT,
  irate        NUMERIC(26, 16),
  ifirstamount NUMERIC(19, 4),
  ifirstdate   TIMESTAMPTZ,
  ibalance     NUMERIC(19, 4)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE cash
  SET
    "title"     = ititle, "dlid" = iDL, "currencyid" = icurrency, "rate" = irate, "firstamount" = ifirstamount,
    "firstdate" = ifirstdate, "balance" = ibalance
  WHERE cashid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeCash(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE cash
  SET
    del = TRUE
  WHERE cashid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newCostCenter(
  uid   BIGINT,
  idlid BIGINT,
  itype INTEGER
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO costcenter
  VALUES (DEFAULT, idlid, itype)
  RETURNING costcenterid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyCostCenter(
  uid   BIGINT,
  iid   BIGINT,
  idlid BIGINT,
  itype INTEGER
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE costcenter
  SET
    "dlid" = idlid, "type" = itype
  WHERE costcenterid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeCostCenter(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE costcenter
  SET
    del = TRUE
  WHERE costcenterid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newParty(
  uid                 BIGINT,
  itype               INTEGER,
  isubtype            INTEGER,
  iname               VARCHAR(250),
  ilastname           VARCHAR(250),
  inameEng            VARCHAR(250),
  ilastnameEng        VARCHAR(250),
  ieconomiccode       VARCHAR(50),
  iidentificationcode VARCHAR(50),
  iwebsite            VARCHAR(250),
  iemail              VARCHAR(250),
  idlid               BIGINT,
  iblacklist          BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO party
  VALUES
    (DEFAULT, itype, isubtype, iname, ilastname, inameEng, ilastnameEng, ieconomiccode, iidentificationcode, iwebsite,
              iemail, idlid, iblacklist)
  RETURNING partyid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyParty(
  uid                 BIGINT,
  iid                 BIGINT,
  itype               INTEGER,
  isubtype            INTEGER,
  iname               VARCHAR(250),
  ilastname           VARCHAR(250),
  inameEng            VARCHAR(250),
  ilastnameEng        VARCHAR(250),
  ieconomiccode       VARCHAR(50),
  iidentificationcode VARCHAR(50),
  iwebsite            VARCHAR(250),
  iemail              VARCHAR(250),
  idlid               BIGINT,
  iblacklist          BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE party
  SET
    "type"       = itype, "subtype" = isubtype, "name" = iname, "lastname" = ilastname, "nameen" = inameEng,
    "lastnameen" = ilastnameEng, "economiccode" = ieconomiccode, "identificationcode" = iidentificationcode,
    "website"    = iwebsite, "email" = iemail, "dlid" = idlid, "isinblacklist" = iblacklist
  WHERE partyid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeParty(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE party
  SET
    del = TRUE
  WHERE partyid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION addPartyBlacklist(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE party
  SET
    isinblacklist = TRUE
  WHERE partyid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removePartyBlacklist(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE party
  SET
    isinblacklist = FALSE
  WHERE partyid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newBank(
  uid    BIGINT,
  ititle VARCHAR(250),
  ilogo  TEXT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO bank
  VALUES (DEFAULT, ititle, ilogo)
  RETURNING bankid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyBank(
  uid    BIGINT,
  iid    BIGINT,
  ititle VARCHAR(250),
  ilogo  TEXT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bank
  SET
    "title" = ititle, "logo" = ilogo
  WHERE bankid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeBank(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bank
  SET
    del = TRUE
  WHERE bankid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newBankAccountType(
  uid        BIGINT,
  ititle     VARCHAR(250),
  ihascheque BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO bankaccounttype
  VALUES (DEFAULT, ititle, ihascheque)
  RETURNING bankaccounttypeid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyBankAccountType(
  uid        BIGINT,
  iid        BIGINT,
  ititle     VARCHAR(250),
  ihascheque BOOLEAN
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bankaccounttype
  SET
    "title" = ititle, "haschequebook" = ihascheque
  WHERE bankaccounttypeid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeBankAccountType(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bankaccounttype
  SET
    del = TRUE
  WHERE bankaccounttypeid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newBankAccount(
  uid                BIGINT,
  ibankbranchid      BIGINT,
  iaccountno         INTEGER,
  ibankaccounttypeid BIGINT,
  idlid              BIGINT,
  icurrencyid        BIGINT,
  irate              DATE,
  ifirstamount       NUMERIC(19, 4),
  ifirstdate         TIMESTAMPTZ,
  ibalance           NUMERIC(19, 4),
  ibillfirstamount   NUMERIC(19, 4),
  iclearformatname   VARCHAR(250),
  iowner             VARCHAR(4000)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO bankaccount
  VALUES (DEFAULT, ibankbranchid, iaccountno, ibankaccounttypeid, idlid, icurrencyid, irate, ifirstamount, ifirstdate,
                   ibalance, ibillfirstamount, iclearformatname, iowner)
  RETURNING bankaccountid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyBankAccount(
  uid                BIGINT,
  iid                BIGINT,
  ibankbranchid      BIGINT,
  iaccountno         INTEGER,
  ibankaccounttypeid BIGINT,
  idlid              BIGINT,
  icurrencyid        BIGINT,
  irate              DATE,
  ibalance           NUMERIC(19, 4),
  ibillfirstamount   NUMERIC(19, 4),
  iclearformatname   VARCHAR(250),
  iowner             VARCHAR(4000)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bankaccount
  SET
    "bankbranchid" = ibankbranchid, "accountno" = iaccountno, "bankaccounttypeid" = ibankaccounttypeid, "dlid" = idlid,
    "currencyid"   = icurrencyid, "rate" = irate,
    "balance"      = ibalance, "billfirstamount" = ibillfirstamount, "clearformatname" = iclearformatname,
    "owner"        = iowner
  WHERE bankaccountid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeBankAccount(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bankaccount
  SET
    del = TRUE
  WHERE bankaccountid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newBankBranch(
  uid         BIGINT,
  ibankid     BIGINT,
  icode       VARCHAR(250),
  ititle      VARCHAR(250),
  ilocationid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO bankbranch
  VALUES (DEFAULT, ibankid, icode, ititle, ilocationid)
  RETURNING bankbranchid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyBankBranch(
  uid         BIGINT,
  iid         BIGINT,
  ibankid     BIGINT,
  icode       VARCHAR(250),
  ititle      VARCHAR(250),
  ilocationid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bankbranch
  SET
    "bankid" = ibankid, "code" = icode, "title" = ititle, "locationid" = ilocationid
  WHERE bankbranchid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeBankBranch(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE bankbranch
  SET
    del = TRUE
  WHERE bankbranchid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newCurrency(
  uid               BIGINT,
  ititle            VARCHAR(250),
  iexchangeunit     INTEGER,
  iprecisioncount   INTEGER,
  iprecisionname    VARCHAR(40),
  iprecisionnameEng VARCHAR(40),
  isign             VARCHAR(40)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO currency
  VALUES (DEFAULT, ititle, iexchangeunit, iprecisioncount, iprecisionname, iprecisionnameEng, isign)
  RETURNING currencyid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyCurrency(
  uid               BIGINT,
  iid               BIGINT,
  ititle            VARCHAR(250),
  iexchangeunit     INTEGER,
  iprecisioncount   INTEGER,
  iprecisionname    VARCHAR(40),
  iprecisionnameEng VARCHAR(40),
  isign             VARCHAR(40)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE currency
  SET
    "title"         = ititle, "exchangeunit" = iexchangeunit, "precisioncount" = iprecisioncount,
    "precisionname" = iprecisionname, "precisionnameen" = iprecisionnameEng, "sign" = isign
  WHERE currencyid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeCurrency(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE currency
  SET
    del = TRUE
  WHERE currencyid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newCurrencyExchangeRate(
  uid            BIGINT,
  icurrency      BIGINT,
  ieffectivedate TIMESTAMPTZ,
  iexchangerate  DATE,
  ifiscalyearid  BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO currencyexchangerate
  VALUES (DEFAULT, icurrency, ieffectivedate, iexchangerate, ifiscalyearid)
  RETURNING currencyexchangerateid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyCurrencyExchangeRate(
  uid            BIGINT,
  iid            BIGINT,
  icurrency      BIGINT,
  ieffectivedate TIMESTAMPTZ,
  iexchangerate  DATE,
  ifiscalyearid  BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE currencyexchangerate
  SET
    "currencyid"   = icurrency, "effectivedate" = ieffectivedate, "exchangerate" = iexchangerate,
    "fiscalyearid" = ifiscalyearid
  WHERE currencyexchangerateid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeCurrencyExchangeRate(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  DELETE FROM currencyexchangerate
  WHERE currencyexchangerateid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION newLocation(
  uid                              BIGINT,
  ititle                           VARCHAR(250),
  icode                            VARCHAR(40),
  iparentid                        BIGINT,
  itype                            INTEGER,
  iministryoffinancecode           VARCHAR(50),
  iministryoffinancecodeoftownship VARCHAR(50)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  INSERT INTO location
  VALUES (DEFAULT, ititle, icode, iparentid, itype, iministryoffinancecode, iministryoffinancecodeoftownship)
  RETURNING locationid
    INTO retval;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION modifyLocation(
  uid                              BIGINT,
  iid                              BIGINT,
  ititle                           VARCHAR(250),
  icode                            VARCHAR(40),
  iparentid                        BIGINT,
  itype                            INTEGER,
  iministryoffinancecode           VARCHAR(50),
  iministryoffinancecodeoftownship VARCHAR(50)
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE location
  SET
    "title"                           = ititle, "code" = icode, "parentid" = iparentid, "type" = itype,
    "ministryoffinancecode"           = iministryoffinancecode,
    "ministryoffinancecodeoftownship" = iministryoffinancecodeoftownship
  WHERE locationid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION removeLocation(
  uid BIGINT,
  iid BIGINT
)
  RETURNS
    INTEGER AS $$
DECLARE retval INTEGER;
BEGIN
  PERFORM versiondata(uid, '');
  UPDATE location
  SET
    del = TRUE
  WHERE locationid = iid;
  GET DIAGNOSTICS retval = ROW_COUNT;
  RETURN retval;
END
$$
LANGUAGE plpgsql;
INSERT INTO partytype (partytypeid, title) VALUES (1, 'Individual');
INSERT INTO partytype (partytypeid, title) VALUES (2, 'Company');
INSERT INTO vouchertype (vouchertypeid, title) VALUES (1, 'General');
INSERT INTO vouchertype (vouchertypeid, title) VALUES (2, 'Other Systems');
INSERT INTO vouchertype (vouchertypeid, title) VALUES (3, 'Close Accounts');
INSERT INTO vouchertype (vouchertypeid, title) VALUES (4, 'Closing');
INSERT INTO vouchertype (vouchertypeid, title) VALUES (5, 'Opening');
INSERT INTO accountbalancetype (accountbalancetypeid, cl, glsl) VALUES (1, 'taraznama', 'Debit Balance');
INSERT INTO accountbalancetype (accountbalancetypeid, cl, glsl) VALUES (2, 'sood o ziyani', 'Credit Balance');
INSERT INTO accountbalancetype (accountbalancetypeid, cl, glsl) VALUES (3, 'entezami', 'dont care');
INSERT INTO costcentertype (costcentertypeid, title) VALUES (1, 'Activity');
INSERT INTO costcentertype (costcentertypeid, title) VALUES (2, 'Ministerial');
INSERT INTO costcentertype (costcentertypeid, title) VALUES (3, 'Distribution and Sale');
INSERT INTO costcentertype (costcentertypeid, title) VALUES (4, 'Overhead');
INSERT INTO locationtype (locationtypeid, title) VALUES (0, 'Location');
INSERT INTO locationtype (locationtypeid, title) VALUES (1, 'Country');
INSERT INTO locationtype (locationtypeid, title) VALUES (2, 'State');
INSERT INTO locationtype (locationtypeid, title) VALUES (3, 'City');
INSERT INTO locationtype (locationtypeid, title) VALUES (4, 'Village');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (1, 'Ministry');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (2, 'Governmental institutions');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (3, 'Governmental Company');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (4, 'Other governmental units');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (5, 'Non-governmental public institutions');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (6, 'Private Sector');
INSERT INTO partysubtype (partysubtypeid, title) VALUES (7, 'Others');