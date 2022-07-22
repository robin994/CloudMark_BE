USE CloudMark;

INSERT INTO `azienda` VALUES ('124e4567-e85b-1fd3-a456-426614474000','markup','32355660906','via lombardia 15','00180','IT94L0300203280726346848321','0612345678','markup@gmail.com','mionome@pecazienda.it', '0612345678'),
                             ('11111111-e85b-1fd3-a456-426614474000','tamtung','22211134543','via carpisa 12','11982','IT33L0300205550726646848321','0766231234','tamtung@gmail.com','tamtung@pecazienda.it', '0766231234'),
                             ('12455557-444b-1333-a886-426699994000','pokia','32544460906','via sempione 223b','22180','IT44D0300203280726346848321','0812555678','tokia@gmail.com','tokia@pecazienda.it', '0552543238');

INSERT into `cliente` VALUES ('123e4567-e89b-12d3-a456-426614174000', 'pippo', '11122233321','via antani 12', '00123', 'IT94L0300203280726346848123','06987654321','pippi@mail.it','pippo@pec.it','06987654321'),
                             ('14444444-e33b-1244-b333-426688884000', 'franco', '22222333431','via giochi 22', '11123', 'IT54L03888888888263448123','09876654321','franco@mail.it','franco@pec.it','09876654321'),
                             ('15555555-e22b-1255-a466-427777174000', 'silvio', '55544432123','via sparta 66', '22123', 'IT34L03009999997263468123','03337654321','silvio@mail.it','silvio@pec.it','03337654321');

INSERT INTO `tipo_contratto`(id_tipo_contratto,nome_tipo_contratto, descrizione) VALUES ('198ef11d-cf73-4245-8469-2ddfa9979acf','indeterminato',NULL),('52fbe812-08f6-11ed-861d-0242ac120002','determinato',NULL);

INSERT INTO `dipendente` VALUES ('124e4567-e85b-1fd3-a456-333322233412','bruno','rossi','123','696','198ef11d-cf73-4245-8469-2ddfa9979acf','brunorossi@gmail.com','1234'),
                                ('12555467-e85b-1fd3-a456-333322233412','andrea','verdi','143','446','52fbe812-08f6-11ed-861d-0242ac120002','andrea@gmail.com','14444'),
                                ('11111167-e85b-1fd3-a456-333322233412','mario','gialli','1444','556','198ef11d-cf73-4245-8469-2ddfa9979acf','mario@gmail.com','13564');

INSERT INTO `tipo_account`(id_tipo_account,nome_tipo_account, lista_funzioni_del_profilo) VALUES ('7e55494c-08f4-11ed-861d-0242ac120002','administrator','admin'),('7e554b54-08f4-11ed-861d-0242ac120002','dipendente','user');

INSERT INTO `commessa` VALUES ('124e4567-e44f-1fd3-a456-330002223341', null, '123e4567-e89b-12d3-a456-426614174000', '124e4567-e85b-1fd3-a456-426614474000', '2022-01-01', '2022-03-30');

INSERT INTO `tipo_presenza`(id_tipo_presenza,nome_tipo_presenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES ('ca34d37e-600c-452e-a8e4-2efb53161812','orario standard',0,NULL),('6dc55260-7150-4f76-8251-adc4c3fc15b4','assenza',0,NULL),('a8fd713d-36e8-440f-81e1-6e7314a3c417','festivo',30,NULL),('b867b283-38a0-4eb3-8df1-55ccb5f310df','malattia',0,NULL);

INSERT INTO `presenza` VALUES ('221e4567-e85b-1fd3-a456-333000003412','124e4567-e85b-1fd3-a456-333322233412','2022-01-01','ca34d37e-600c-452e-a8e4-2efb53161812','124e4567-e44f-1fd3-a456-330002223341',50);

INSERT INTO `azienda_cliente` VALUES ('124e4567-e85b-1fd3-a456-426614474000','123e4567-e89b-12d3-a456-426614174000'),
                                     ('11111111-e85b-1fd3-a456-426614474000','14444444-e33b-1244-b333-426688884000'),
                                     ('12455557-444b-1333-a886-426699994000','15555555-e22b-1255-a466-427777174000');

INSERT into `commessa_dipendente` VALUES ('124e4567-e44f-1fd3-a456-330002223341','124e4567-e85b-1fd3-a456-333322233412', 200);

INSERT INTO cloudmark.account (id_account,`user`,password,abilitato,id_tipo_account) VALUES
	 ('1614c896-ae46-42e4-b31a-ae395cd198cf','andrea',0xFC0CCB2C212AB587FEA3FC0737C38BA9B32C9517A482C3C6B2196764D564C312,0,'7e554b54-08f4-11ed-861d-0242ac120002'),
	 ('28daa75b-7ea2-4f2c-b771-525a06cd7d9f','bruno',0xF2FA2BD38827B4D55F7B34DE56D73F80A08EC77A08634CC9D5E6AA2A784AEE0A,1,'7e55494c-08f4-11ed-861d-0242ac120002'),
	 ('72d2b7fd-cd54-4714-85fd-441325f7247b','mario',0x7F7A8A9E8A31C2EA4CB68F451600DF2F79A220D02E251C841559FAA639082525,0,'7e554b54-08f4-11ed-861d-0242ac120002');

INSERT INTO cloudmark.saltini (id_account,salt) VALUES
	 ('1614c896-ae46-42e4-b31a-ae395cd198cf',0xA87B8C842114B10BF1AA6A267E59D97C9DC4720E2A9E841EADF879D1A7243E0A),
	 ('28daa75b-7ea2-4f2c-b771-525a06cd7d9f',0x0F50F65A3F4B4AE4AB073E400E24BA0A21B315A79D60ADF0D41342BAC7EAA076),
	 ('72d2b7fd-cd54-4714-85fd-441325f7247b',0xAA6B77AA918E8F9E748C3CD7EFCEDAA196284B8BDAA73F94FDC669421C960084);

INSERT INTO `account_dipendente` VALUES ('28daa75b-7ea2-4f2c-b771-525a06cd7d9f','124e4567-e85b-1fd3-a456-333322233412'),
                                        ('1614c896-ae46-42e4-b31a-ae395cd198cf','12555467-e85b-1fd3-a456-333322233412'),
                                        ('72d2b7fd-cd54-4714-85fd-441325f7247b','11111167-e85b-1fd3-a456-333322233412');

INSERT INTO `dipendente_azienda` VALUES ('124e4567-e85b-1fd3-a456-333322233412', '124e4567-e85b-1fd3-a456-426614474000', '2022-01-01', '000', '2022-05-05'),
                                        ('12555467-e85b-1fd3-a456-333322233412', '124e4567-e85b-1fd3-a456-426614474000', '2022-05-15', '001', '2022-08-08'),
										('11111167-e85b-1fd3-a456-333322233412', '12455557-444b-1333-a886-426699994000', '2022-03-21', '002', '2022-05-06');

COMMIT;





