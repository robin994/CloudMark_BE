INSERT INTO `azienda` VALUES (1,'markup','32355660906','via lombardia 15','00180','IT94L0300203280726346848321','0612345678','markup@gmail.com','mionome@pecazienda.it', '0612345678');

INSERT into `cliente` VALUES (1, 'pippo', 'aaabbbcccdd','via antani 12', '00123', 'IT94L0300203280726346848123','06987654321','pippi@mail.it','pippo@pec.it','06987654321');

INSERT INTO `tipo_contratto`(nome_tipocontratto, descrizione) VALUES ('indeterminato',NULL);

INSERT INTO `dipendente` VALUES (1,'bruno','rossi','123','696','indeterminato','brunorossi@gmail.com','1234');

INSERT INTO `tipo_account`(nome_tipoAccount, lista_funzioni_del_profilo) VALUES ('administrator','admin'),('dipendente','user');

INSERT INTO `account` VALUES (1,'bruno','pop',0,'administrator'),(2,'mario','mem',1,'dipendente');

INSERT INTO `commessa` VALUES (1, null, 1, 1, '2022-01-01', '2022-03-30');

INSERT INTO `tipo_presenza`(nome_tipoPresenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES ('orario standard',0,NULL),('assenza',0,NULL),('festivo',30,NULL),('malattia',0,NULL);

INSERT INTO `presenza` VALUES (1,'2022-01-01','festivo',1,50);

INSERT INTO `account_dipendente` VALUES (1, 1);

INSERT INTO `azienda_cliente` VALUES (1, 1);

INSERT into `commessa_dipendente` VALUES (1, 1, 200);

INSERT INTO `dipendente_azienda` VALUES (1, 1, '2022-01-01', '000', '2022-05-05');