USE CloudMark;

INSERT INTO `azienda` VALUES (1,'markup','32355660906','via lombardia 15','00180','IT94L0300203280726346848321','0612345678','markup@gmail.com','mionome@pecazienda.it', '0612345678');

INSERT into `cliente` VALUES ('123e4567-e89b-12d3-a456-426614174000', 'pippo', 'aaabbbcccdd','via antani 12', '00123', 'IT94L0300203280726346848123','06987654321','pippi@mail.it','pippo@pec.it','06987654321');

INSERT INTO `tipo_contratto`(id_tipo_contratto,nome_tipo_contratto, descrizione) VALUES (1,'indeterminato',NULL),(2,'determinato',NULL);

INSERT INTO `dipendente` VALUES (1,'bruno','rossi','123','696',1,'brunorossi@gmail.com','1234');

INSERT INTO `tipo_account`(id_tipo_account,nome_tipo_account, lista_funzioni_del_profilo) VALUES (1,'administrator','admin'),(2,'dipendente','user');

INSERT INTO `account` VALUES (1,'bruno','pop',0,1),(2,'mario','mem',1,2);

INSERT INTO `commessa` VALUES (1, null, '123e4567-e89b-12d3-a456-426614174000', 1, '2022-01-01', '2022-03-30');

INSERT INTO `tipo_presenza`(id_tipo_presenza,nome_tipo_presenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES (1,'orario standard',0,NULL),(2,'assenza',0,NULL),(3,'festivo',30,NULL),(4,'malattia',0,NULL);

INSERT INTO `presenza` VALUES (1,'2022-01-01',3,1,50);

INSERT INTO `account_dipendente` VALUES (1, 1);

INSERT INTO `azienda_cliente` VALUES (1,'123e4567-e89b-12d3-a456-426614174000');

INSERT into `commessa_dipendente` VALUES (1, 1, 200);

INSERT INTO `dipendente_azienda` VALUES (1, 1, '2022-01-01', '000', '2022-05-05');

COMMIT;