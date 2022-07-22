USE CloudMark;

INSERT INTO `azienda` VALUES ('124e4567-e85b-1fd3-a456-426614474000','markup','32355660906','via lombardia 15','00180','IT94L0300203280726346848321','0612345678','markup@gmail.com','mionome@pecazienda.it', '0612345678');

INSERT into `cliente` VALUES ('123e4567-e89b-12d3-a456-426614174000', 'pippo', 'aaabbbcccdd','via antani 12', '00123', 'IT94L0300203280726346848123','06987654321','pippi@mail.it','pippo@pec.it','06987654321');

INSERT INTO `tipo_contratto`(id_tipo_contratto,nome_tipo_contratto, descrizione) VALUES ('198ef11d-cf73-4245-8469-2ddfa9979acf','indeterminato',NULL),('52fbe812-08f6-11ed-861d-0242ac120002','determinato',NULL);

INSERT INTO `dipendente` VALUES ('124e4567-e85b-1fd3-a456-333322233412','bruno','rossi','123','696','198ef11d-cf73-4245-8469-2ddfa9979acf','brunorossi@gmail.com','1234');

INSERT INTO `dipendente` VALUES ('12555467-e85b-1fd3-a456-333322233412','andrea','verdi','143','123','198ef11d-cf73-4245-8469-2ddfa9979acf','andrea@gmail.com','14444');
INSERT INTO `dipendente` VALUES ('2275eb94-4fa1-438c-b663-c429787c2f42','giulio','regeni','258','456','198ef11d-cf73-4245-8469-2ddfa9979acf','giulio@gmail.com','330aa');
INSERT INTO `dipendente` VALUES ('ae699909-1869-419f-9297-94125661d413','marco','nero','716','789','52fbe812-08f6-11ed-861d-0242ac120002','marco@gmail.com','nergo');
INSERT INTO `dipendente` VALUES ('a8daffdf-d4d0-444b-9419-b1e64796a997','nicola','proibito','255','012','52fbe812-08f6-11ed-861d-0242ac120002','nicola@gmail.com','55555');
INSERT INTO `dipendente` VALUES ('63879535-c9ae-4e9b-b3d7-97b1265d8636','destro','rinaldi','128','345','52fbe812-08f6-11ed-861d-0242ac120002','destro@gmail.com','aabbc');

INSERT INTO `tipo_account`(id_tipo_account,nome_tipo_account, lista_funzioni_del_profilo) VALUES ('7e55494c-08f4-11ed-861d-0242ac120002','administrator','admin'),('7e554b54-08f4-11ed-861d-0242ac120002','dipendente','user');

INSERT INTO `commessa` VALUES ('124e4567-e44f-1fd3-a456-330002223341', null, '123e4567-e89b-12d3-a456-426614174000', '124e4567-e85b-1fd3-a456-426614474000', '2022-01-01', '2022-03-30');

INSERT INTO `tipo_presenza`(id_tipo_presenza, nome_tipo_presenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES ('ca34d37e-600c-452e-a8e4-2efb53161812', 'orario standard', 0, NULL),('6dc55260-7150-4f76-8251-adc4c3fc15b4','assenza',0,NULL),('a8fd713d-36e8-440f-81e1-6e7314a3c417','festivo',30,NULL),('b867b283-38a0-4eb3-8df1-55ccb5f310df','malattia',0,NULL);

INSERT INTO `presenza` VALUES ('221e4567-e85b-1fd3-a456-333000003412','124e4567-e85b-1fd3-a456-333322233412','2022-01-01','b867b283-38a0-4eb3-8df1-55ccb5f310df','124e4567-e44f-1fd3-a456-330002223341',50);
INSERT INTO `presenza` VALUES ('1d332db5-18ba-44aa-b6dd-155294f8c299','2275eb94-4fa1-438c-b663-c429787c2f42','2022-02-01','b867b283-38a0-4eb3-8df1-55ccb5f310df','124e4567-e44f-1fd3-a456-330002223341',50);
INSERT INTO `presenza` VALUES ('f2a711d6-123d-47ca-97c6-de2e52842146','ae699909-1869-419f-9297-94125661d413','2022-03-01','b867b283-38a0-4eb3-8df1-55ccb5f310df','124e4567-e44f-1fd3-a456-330002223341',50);
INSERT INTO `presenza` VALUES ('ad13ddf8-2fc3-4033-bb4b-e0847dc63454','a8daffdf-d4d0-444b-9419-b1e64796a997','2022-04-01','b867b283-38a0-4eb3-8df1-55ccb5f310df','124e4567-e44f-1fd3-a456-330002223341',50);
INSERT INTO `presenza` VALUES ('489c7a7d-d54d-4e9e-8b7d-b0f8f6d8e1d1','63879535-c9ae-4e9b-b3d7-97b1265d8636','2022-05-01','b867b283-38a0-4eb3-8df1-55ccb5f310df','124e4567-e44f-1fd3-a456-330002223341',50);

INSERT INTO `azienda_cliente` VALUES ('124e4567-e85b-1fd3-a456-426614474000','123e4567-e89b-12d3-a456-426614174000');

INSERT into `commessa_dipendente` VALUES ('124e4567-e44f-1fd3-a456-330002223341','124e4567-e85b-1fd3-a456-333322233412', 200);

INSERT INTO cloudmark.account (id_account,`user`,password,abilitato,id_tipo_account) VALUES
	 ('e55917e1-0e9f-40b2-92ae-c880328aa110','bruno',0x324517FB662F555859C2BF73A5EB9D43C5DF35B2AA522DDC6F2CE2AEBB440EC0,1,'7e55494c-08f4-11ed-861d-0242ac120002');

INSERT INTO cloudmark.saltini (id_account,salt) VALUES
	 ('e55917e1-0e9f-40b2-92ae-c880328aa110',0x50A4AFAC90CA91520D1E3586918699D7810B49683D424C6E444670A52D0E5F9E);

INSERT INTO `account_dipendente` VALUES ('e55917e1-0e9f-40b2-92ae-c880328aa110','124e4567-e85b-1fd3-a456-333322233412');

INSERT INTO `dipendente_azienda` VALUES ('124e4567-e85b-1fd3-a456-333322233412', '124e4567-e85b-1fd3-a456-426614474000', '2022-01-01', '000', '2022-05-05');

COMMIT;