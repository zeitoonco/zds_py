CREATE TABLE account
(
  accountid             BIGINT PRIMARY KEY    NOT NULL,
  parentid              BIGINT,
  type                  INTEGER               NOT NULL,
  code                  VARCHAR(40)           NOT NULL,
  title                 VARCHAR(250)          NOT NULL,
  title2                VARCHAR(250),
  isactive              BOOLEAN DEFAULT TRUE  NOT NULL,
  cashflowcategory      INTEGER,
  openingbalance        NUMERIC(19, 4),
  balancetype           INTEGER               NOT NULL,
  hasbalancetypecheck   BOOLEAN DEFAULT FALSE NOT NULL,
  hasdl                 BOOLEAN               NOT NULL,
  hascurrency           BOOLEAN DEFAULT FALSE NOT NULL,
  hascurrencyconversion BOOLEAN DEFAULT FALSE NOT NULL,
  hastracking           BOOLEAN DEFAULT FALSE NOT NULL,
  hastrackingcheck      BOOLEAN DEFAULT FALSE NOT NULL,
  version               BIGINT                NOT NULL,
  del                   BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkaccount555592 FOREIGN KEY (parentid) REFERENCES account (accountid),
  CONSTRAINT fkaccount464978 FOREIGN KEY (balancetype) REFERENCES accountbalancetype (accountbalancetypeid)
);
CREATE UNIQUE INDEX account_code ON account (code);
CREATE UNIQUE INDEX account_version_key ON account (version);
CREATE TABLE accountbalancetype
(
  accountbalancetypeid INTEGER PRIMARY KEY NOT NULL,
  cl                   VARCHAR(250),
  glsl                 VARCHAR(250)
);
CREATE TABLE accounttopic
(
  topicid   BIGINT NOT NULL,
  accountid BIGINT NOT NULL,
  CONSTRAINT accounttopic_pkey PRIMARY KEY (topicid, accountid),
  CONSTRAINT fkaccounttop743736 FOREIGN KEY (topicid) REFERENCES topic (topicid),
  CONSTRAINT fkaccounttop657317 FOREIGN KEY (accountid) REFERENCES account (accountid)
);
CREATE TABLE bank
(
  bankid  BIGINT PRIMARY KEY    NOT NULL,
  title   VARCHAR(250)          NOT NULL,
  logo    BYTEA,
  version BIGINT                NOT NULL,
  del     BOOLEAN DEFAULT FALSE NOT NULL
);
CREATE TABLE bankaccount
(
  bankaccountid     BIGINT PRIMARY KEY       NOT NULL,
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
  clearformatname   VARCHAR(250),
  owner             VARCHAR(4000),
  version           BIGINT                   NOT NULL,
  del               BOOLEAN DEFAULT FALSE    NOT NULL,
  CONSTRAINT fkbankaccoun731590 FOREIGN KEY (bankbranchid) REFERENCES bankbranch (bankbranchid),
  CONSTRAINT fkbankaccoun586688 FOREIGN KEY (bankaccounttypeid) REFERENCES bankaccounttype (bankaccounttypeid),
  CONSTRAINT fkbankaccoun510318 FOREIGN KEY (dlid) REFERENCES dl (dlid),
  CONSTRAINT fkbankaccoun599249 FOREIGN KEY (currencyid) REFERENCES currency (currencyid)
);
CREATE TABLE bankaccounttype
(
  bankaccounttypeid BIGINT PRIMARY KEY    NOT NULL,
  title             VARCHAR(250)          NOT NULL,
  haschequebook     BOOLEAN               NOT NULL,
  version           BIGINT                NOT NULL,
  del               BOOLEAN DEFAULT FALSE NOT NULL
);
CREATE TABLE bankbranch
(
  bankbranchid BIGINT PRIMARY KEY    NOT NULL,
  bankid       BIGINT                NOT NULL,
  code         VARCHAR(250)          NOT NULL,
  title        VARCHAR(250)          NOT NULL,
  locationid   BIGINT                NOT NULL,
  version      BIGINT                NOT NULL,
  del          BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkbankbranch684888 FOREIGN KEY (bankid) REFERENCES bank (bankid),
  CONSTRAINT fkbankbranch970953 FOREIGN KEY (locationid) REFERENCES location (locationid)
);
CREATE TABLE cash
(
  cashid      BIGINT PRIMARY KEY       NOT NULL,
  title       VARCHAR(250)             NOT NULL,
  dlid        BIGINT                   NOT NULL,
  currencyid  BIGINT                   NOT NULL,
  rate        NUMERIC(26, 16)          NOT NULL,
  firstamount NUMERIC(19, 4)           NOT NULL,
  firstdate   TIMESTAMP WITH TIME ZONE NOT NULL,
  balance     NUMERIC(19, 4)           NOT NULL,
  version     BIGINT                   NOT NULL,
  del         BOOLEAN DEFAULT FALSE    NOT NULL,
  CONSTRAINT fkcash297383 FOREIGN KEY (dlid) REFERENCES dl (dlid),
  CONSTRAINT fkcash812184 FOREIGN KEY (currencyid) REFERENCES currency (currencyid)
);
CREATE TABLE category
(
  categoryid BIGINT PRIMARY KEY NOT NULL,
  type       INTEGER            NOT NULL,
  title      VARCHAR(250)       NOT NULL,
  CONSTRAINT fkcategory276962 FOREIGN KEY (type) REFERENCES categorytype (categorytypeid)
);
CREATE TABLE categorytype
(
  categorytypeid INTEGER PRIMARY KEY NOT NULL,
  title          VARCHAR(250)        NOT NULL
);
CREATE TABLE config
(
  name    VARCHAR(255) PRIMARY KEY NOT NULL,
  value   TEXT,
  version BIGINT
);
CREATE TABLE costcenter
(
  costcenterid BIGINT PRIMARY KEY    NOT NULL,
  dlid         BIGINT                NOT NULL,
  type         INTEGER               NOT NULL,
  version      BIGINT                NOT NULL,
  del          BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkcostcenter478444 FOREIGN KEY (dlid) REFERENCES dl (dlid),
  CONSTRAINT fkcostcenter779458 FOREIGN KEY (type) REFERENCES costcentertype (costcentertypeid)
);
CREATE TABLE costcentertype
(
  costcentertypeid INTEGER PRIMARY KEY NOT NULL,
  title            VARCHAR(250)        NOT NULL
);
CREATE TABLE currency
(
  currencyid      BIGINT PRIMARY KEY    NOT NULL,
  title           VARCHAR(250)          NOT NULL,
  exchangeunit    INTEGER               NOT NULL,
  precisioncount  INTEGER               NOT NULL,
  precisionname   VARCHAR(40),
  precisionnameen VARCHAR(40),
  sign            VARCHAR(40)           NOT NULL,
  version         BIGINT                NOT NULL,
  del             BOOLEAN DEFAULT FALSE NOT NULL
);
CREATE TABLE currencyexchangerate
(
  currencyexchangerateid BIGINT PRIMARY KEY NOT NULL,
  currencyid             BIGINT             NOT NULL,
  effectivedate          TIMESTAMP WITH TIME ZONE,
  exchangerate           NUMERIC(24, 16),
  version                BIGINT,
  fiscalyearid           BIGINT             NOT NULL,
  CONSTRAINT fkcurrencyex68234 FOREIGN KEY (currencyid) REFERENCES currency (currencyid),
  CONSTRAINT fkcurrencyex54543 FOREIGN KEY (fiscalyearid) REFERENCES fiscalyear (fiscalyearid)
);
CREATE TABLE dl
(
  dlid     BIGINT PRIMARY KEY    NOT NULL,
  code     VARCHAR(40)           NOT NULL,
  title    VARCHAR(250)          NOT NULL,
  title2   VARCHAR(250),
  type     INTEGER               NOT NULL,
  isactive BOOLEAN DEFAULT TRUE  NOT NULL,
  version  BIGINT                NOT NULL,
  del      BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkdl70390 FOREIGN KEY (type) REFERENCES dltype (dltypeid)
);
CREATE UNIQUE INDEX dl_code ON dl (code);
CREATE TABLE dltype
(
  dltypeid INTEGER PRIMARY KEY NOT NULL,
  title    VARCHAR(250)        NOT NULL
);
CREATE TABLE fiscalyear
(
  fiscalyearid BIGINT PRIMARY KEY    NOT NULL,
  title        VARCHAR(250)          NOT NULL,
  startdate    DATE                  NOT NULL,
  enddate      DATE                  NOT NULL,
  status       INTEGER               NOT NULL,
  version      BIGINT                NOT NULL,
  del          BOOLEAN DEFAULT FALSE NOT NULL
);
CREATE TABLE glvoucher
(
  glvoucherid  BIGINT PRIMARY KEY                     NOT NULL,
  number       INTEGER                                NOT NULL,
  "Date"       TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  fiscalyearid BIGINT                                 NOT NULL,
  version      BIGINT                                 NOT NULL,
  del          BOOLEAN DEFAULT FALSE                  NOT NULL,
  CONSTRAINT fkglvoucher692499 FOREIGN KEY (fiscalyearid) REFERENCES fiscalyear (fiscalyearid)
);
CREATE TABLE glvoucheritem
(
  glvoucherid BIGINT                NOT NULL,
  voucherid   BIGINT                NOT NULL,
  version     BIGINT                NOT NULL,
  del         BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT glvoucheritem_pkey PRIMARY KEY (glvoucherid, voucherid),
  CONSTRAINT fkglvoucheri2846 FOREIGN KEY (glvoucherid) REFERENCES glvoucher (glvoucherid),
  CONSTRAINT fkglvoucheri957496 FOREIGN KEY (voucherid) REFERENCES voucher (voucherid)
);
CREATE TABLE location
(
  locationid                      BIGINT PRIMARY KEY    NOT NULL,
  title                           VARCHAR(250)          NOT NULL,
  code                            VARCHAR(40)           NOT NULL,
  parentid                        BIGINT,
  type                            INTEGER               NOT NULL,
  ministryoffinancecode           VARCHAR(50)           NOT NULL,
  ministryoffinancecodeoftownship VARCHAR(50)           NOT NULL,
  version                         BIGINT                NOT NULL,
  del                             BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fklocation24558 FOREIGN KEY (type) REFERENCES locationtype (locationtypeid)
);
CREATE TABLE locationtype
(
  locationtypeid INTEGER PRIMARY KEY NOT NULL,
  title          VARCHAR(250)        NOT NULL
);
CREATE TABLE openingoperation
(
  openingoperationid BIGINT PRIMARY KEY                     NOT NULL,
  "Date"             TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  accountid          BIGINT                                 NOT NULL,
  voucherid          BIGINT                                 NOT NULL,
  description        VARCHAR(250),
  version            BIGINT                                 NOT NULL,
  del                BOOLEAN DEFAULT FALSE                  NOT NULL,
  CONSTRAINT fkopeningope300419 FOREIGN KEY (accountid) REFERENCES account (accountid),
  CONSTRAINT fkopeningope948549 FOREIGN KEY (voucherid) REFERENCES voucher (voucherid)
);
CREATE TABLE openingoperationitem
(
  openingoperationitemid BIGINT PRIMARY KEY    NOT NULL,
  openingoperationid     BIGINT                NOT NULL,
  recordtype             VARCHAR(400)          NOT NULL,
  recordid               BIGINT                NOT NULL,
  checked                BOOLEAN,
  version                BIGINT                NOT NULL,
  del                    BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkopeningope268300 FOREIGN KEY (openingoperationid) REFERENCES openingoperation (openingoperationid)
);
CREATE TABLE party
(
  partyid            BIGINT PRIMARY KEY    NOT NULL,
  type               INTEGER               NOT NULL,
  subtype            INTEGER               NOT NULL,
  name               VARCHAR(250)          NOT NULL,
  lastname           VARCHAR(250),
  nameen             VARCHAR(250),
  lastnameen         VARCHAR(250),
  economiccode       VARCHAR(50),
  identificationcode VARCHAR(50),
  website            VARCHAR(250),
  email              VARCHAR(250),
  dlid               BIGINT                NOT NULL,
  isinblacklist      BOOLEAN               NOT NULL,
  avatar             BYTEA,
  version            BIGINT                NOT NULL,
  del                BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkparty675290 FOREIGN KEY (type) REFERENCES partytype (partytypeid),
  CONSTRAINT fkparty274801 FOREIGN KEY (subtype) REFERENCES partysubtype (partysubtype),
  CONSTRAINT fkparty89253 FOREIGN KEY (dlid) REFERENCES dl (dlid)
);
CREATE TABLE partysubtype
(
  partysubtype INTEGER PRIMARY KEY NOT NULL,
  title        VARCHAR(250)        NOT NULL
);
CREATE TABLE partytype
(
  partytypeid INTEGER PRIMARY KEY NOT NULL,
  title       VARCHAR(250)        NOT NULL
);
CREATE TABLE tables
(
  tableid BIGINT PRIMARY KEY NOT NULL,
  scheme  VARCHAR(40)        NOT NULL,
  name    VARCHAR(255)       NOT NULL
);
CREATE TABLE topic
(
  topicid    BIGINT PRIMARY KEY NOT NULL,
  title      VARCHAR(250)       NOT NULL,
  categoryid BIGINT             NOT NULL,
  CONSTRAINT fktopic795702 FOREIGN KEY (categoryid) REFERENCES category (categoryid)
);
CREATE TABLE version
(
  tableid       BIGINT                                 NOT NULL,
  rowid         BIGINT                                 NOT NULL,
  version       BIGINT                                 NOT NULL,
  userid        BIGINT                                 NOT NULL,
  submitdate    TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  description   VARCHAR(1024),
  rowdata       HSTORE,
  changedfields HSTORE,
  equery        TEXT,
  action        TEXT,
  CONSTRAINT version_pkey PRIMARY KEY (tableid, rowid, version),
  CONSTRAINT fkversion246025 FOREIGN KEY (tableid) REFERENCES tables (tableid)
);
CREATE TABLE voucher
(
  voucherid       BIGINT PRIMARY KEY                     NOT NULL,
  number          INTEGER                                NOT NULL,
  "Date"          TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
  referencenumber INTEGER                                NOT NULL,
  secondarynumber INTEGER,
  state           INTEGER                                NOT NULL,
  type            INTEGER                                NOT NULL,
  fiscalyearid    BIGINT                                 NOT NULL,
  description     VARCHAR(250),
  dailynumber     INTEGER                                NOT NULL,
  issuersystem    BIGINT,
  version         BIGINT                                 NOT NULL,
  del             BOOLEAN DEFAULT FALSE                  NOT NULL,
  CONSTRAINT fkvoucher87077 FOREIGN KEY (type) REFERENCES vouchertype (vouchertypeid),
  CONSTRAINT fkvoucher956379 FOREIGN KEY (fiscalyearid) REFERENCES fiscalyear (fiscalyearid)
);
CREATE TABLE voucheritem
(
  voucheritemid  BIGINT PRIMARY KEY    NOT NULL,
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
  trackingnumber VARCHAR(40),
  trackingdate   TIMESTAMP WITH TIME ZONE,
  description    VARCHAR(250),
  version        BIGINT                NOT NULL,
  del            BOOLEAN DEFAULT FALSE NOT NULL,
  CONSTRAINT fkvoucherite380598 FOREIGN KEY (voucherid) REFERENCES voucher (voucherid),
  CONSTRAINT fkvoucherite28729 FOREIGN KEY (accountid) REFERENCES account (accountid),
  CONSTRAINT fkvoucherite22053 FOREIGN KEY (dlid) REFERENCES dl (dlid),
  CONSTRAINT fkvoucherite87515 FOREIGN KEY (currencyid) REFERENCES currency (currencyid)
);
CREATE TABLE vouchertype
(
  vouchertypeid INTEGER PRIMARY KEY NOT NULL,
  title         VARCHAR(250)        NOT NULL
);