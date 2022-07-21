USE CloudMark;

INSERT INTO `azienda` VALUES ('124e4567-e85b-1fd3-a456-426614474000','markup','32355660906','via lombardia 15','00180','IT94L0300203280726346848321','0612345678','markup@gmail.com','mionome@pecazienda.it', '0612345678');

INSERT into `cliente` VALUES ('123e4567-e89b-12d3-a456-426614174000', 'pippo', 'aaabbbcccdd','via antani 12', '00123', 'IT94L0300203280726346848123','06987654321','pippi@mail.it','pippo@pec.it','06987654321');

INSERT INTO `tipo_contratto`(id_tipo_contratto,nome_tipo_contratto, descrizione) VALUES (1,'indeterminato',NULL),(2,'determinato',NULL);

INSERT INTO `dipendente` VALUES ('124e4567-e85b-1fd3-a456-333322233412','bruno','rossi','123','696',1,'brunorossi@gmail.com','1234');

INSERT INTO `dipendente` VALUES ('12555467-e85b-1fd3-a456-333322233412','andrea','verdi','143','446',1,'andrea@gmail.com','14444');

INSERT INTO `tipo_account`(id_tipo_account,nome_tipo_account, lista_funzioni_del_profilo) VALUES ('7e55494c-08f4-11ed-861d-0242ac120002','administrator','admin'),('7e554b54-08f4-11ed-861d-0242ac120002','dipendente','user');

INSERT INTO `commessa` VALUES ('124e4567-e44f-1fd3-a456-330002223341', null, '123e4567-e89b-12d3-a456-426614174000', '124e4567-e85b-1fd3-a456-426614474000', '2022-01-01', '2022-03-30');

INSERT INTO `tipo_presenza`(id_tipo_presenza,nome_tipo_presenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES (1,'orario standard',0,NULL),(2,'assenza',0,NULL),(3,'festivo',30,NULL),(4,'malattia',0,NULL);

INSERT INTO `presenza` VALUES ('221e4567-e85b-1fd3-a456-333000003412','124e4567-e85b-1fd3-a456-333322233412','2022-01-01',3,'124e4567-e44f-1fd3-a456-330002223341',50);

INSERT INTO `azienda_cliente` VALUES ('124e4567-e85b-1fd3-a456-426614474000','123e4567-e89b-12d3-a456-426614174000');

INSERT into `commessa_dipendente` VALUES ('124e4567-e44f-1fd3-a456-330002223341','124e4567-e85b-1fd3-a456-333322233412', 200);

INSERT INTO cloudmark.account (id_account,`user`,password,abilitato,id_tipo_account) VALUES
	 ('e55917e1-0e9f-40b2-92ae-c880328aa110','bruno',0x324517FB662F555859C2BF73A5EB9D43C5DF35B2AA522DDC6F2CE2AEBB440EC0,1,'7e55494c-08f4-11ed-861d-0242ac120002');

INSERT INTO cloudmark.saltini (id_account,salt) VALUES
	 ('e55917e1-0e9f-40b2-92ae-c880328aa110',0x50A4AFAC90CA91520D1E3586918699D7810B49683D424C6E444670A52D0E5F9E);

INSERT INTO `account_dipendente` VALUES ('e55917e1-0e9f-40b2-92ae-c880328aa110','124e4567-e85b-1fd3-a456-333322233412');

INSERT INTO `dipendente_azienda` VALUES ('124e4567-e85b-1fd3-a456-333322233412', '124e4567-e85b-1fd3-a456-426614474000', '2022-01-01', '000', '2022-05-05');

COMMIT;