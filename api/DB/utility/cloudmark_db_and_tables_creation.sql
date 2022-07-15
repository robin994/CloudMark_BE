CREATE DATABASE IF NOT EXISTS cloudmark;

USE cloudmark;

DROP TABLE IF EXISTS `azienda`;
CREATE TABLE `azienda` (
  `id_azienda` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(90) DEFAULT NULL,
  `p_iva` char(11) DEFAULT NULL,
  `indirizzo` varchar(90) DEFAULT NULL,
  `cap` char(5) DEFAULT NULL,
  `iban` char(27) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `pec` varchar(45) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_azienda`),
  UNIQUE KEY `nome_UNIQUE` (`nome`)
);

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(90) DEFAULT NULL,
  `p_iva` char(11) DEFAULT NULL,
  `indirizzo` varchar(90) DEFAULT NULL,
  `cap` char(5) DEFAULT NULL,
  `iban` char(27) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `pec` varchar(90) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
);

DROP TABLE IF EXISTS `tipoContratto`;
CREATE TABLE `tipo_contratto` (
  `id_tipoContratto` int NOT NULL AUTO_INCREMENT,
  `nome_tipocontratto` varchar(45) NOT NULL,
  `descrizione` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_tipoContratto`)
);

DROP TABLE IF EXISTS `dipendente`;
CREATE TABLE `dipendente` (
  `id_dipendente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `cognome` varchar(45) DEFAULT NULL,
  `cf` varchar(16) NOT NULL,
  `iban` varchar(45) NOT NULL,
  `id_tipoContratto` int NOT NULL,
  `email` varchar(90) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_dipendente`),
  UNIQUE KEY `cf_UNIQUE` (`cf`),
  KEY `tipo_contratto_idx` (`id_tipoContratto`),
  KEY `fk_dipendente_tipo_contratto_idx` (`id_tipoContratto`),
  CONSTRAINT `dipendente_ibfk_1` FOREIGN KEY (`id_tipoContratto`) REFERENCES `id_tipoContratto` (`id_tipoContratto`)
);

DROP TABLE IF EXISTS `tipoAccount`;
CREATE TABLE `tipoAccount` (
  `id_tipoAccount` int NOT NULL AUTO_INCREMENT,
  `nome_id_tipoAccount` varchar(45) NOT NULL,
  `lista_funzioni_del_profilo` text,
  PRIMARY KEY (`id_tipoAccount`)
);


DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id_account` int NOT NULL AUTO_INCREMENT,
  `user` varchar(45) NOT NULL,
  `password` char(64) NOT NULL,
  `abilitato` tinyint(1) DEFAULT NULL,
  `id_tipoAccount` int NOT NULL,
  PRIMARY KEY (`id_account`),
  UNIQUE KEY `user_UNIQUE` (`user`),
  KEY `id_tipoAccount` (`id_tipoAccount`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`id_tipoAccount`) REFERENCES `id_tipoAccount` (`id_tipoAccount`)
);

DROP TABLE IF EXISTS `commessa`;
CREATE TABLE `commessa` (
  `id_commessa` int NOT NULL AUTO_INCREMENT,
  `descrizione` varchar(255) DEFAULT NULL,
  `id_cliente` int NOT NULL,
  `id_azienda` int NOT NULL,
  `data_inizio` date NOT NULL,
  `data_fine` date NOT NULL,
  PRIMARY KEY (`id_commessa`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_azienda` (`id_azienda`),
  CONSTRAINT `commessa_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `commessa_ibfk_2` FOREIGN KEY (`id_azienda`) REFERENCES `azienda` (`id_azienda`)
);

DROP TABLE IF EXISTS `tipoPresenza`;
CREATE TABLE `tipoPresenza` (
  `id_tipoPresenza` int NOT NULL AUTO_INCREMENT,
  `nome_id_tipoPresenza` varchar(45) NOT NULL,
  `perc_maggiorazione_paga_oraria` int DEFAULT NULL,
  `paga_oraria` int DEFAULT NULL,
  PRIMARY KEY (`id_tipoPresenza`)
);

DROP TABLE IF EXISTS `presenza`;
CREATE TABLE `presenza` (
  `id_dipendente` int NOT NULL,
  `data` date NOT NULL,
  `id_tipoPresenza` int NOT NULL,
  `id_commessa` int NOT NULL,
  `ore` int DEFAULT NULL,
  PRIMARY KEY (`id_dipendente`,`data`,`id_tipoPresenza`),
  KEY `id_tipoPresenza` (`id_tipoPresenza`),
  KEY `id_commessa` (`id_commessa`),
  CONSTRAINT `presenza_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `presenza_ibfk_2` FOREIGN KEY (`id_tipoPresenza`) REFERENCES `id_tipoPresenza` (`id_tipoPresenza`),
  CONSTRAINT `presenza_ibfk_3` FOREIGN KEY (`id_commessa`) REFERENCES `commessa` (`id_commessa`)
);

DROP TABLE IF EXISTS `account_dipendente`;
CREATE TABLE `account_dipendente` (
  `id_dipendente` int NOT NULL,
  `id_account` int NOT NULL,
  PRIMARY KEY (`id_dipendente`,`id_account`),
  KEY `id_account` (`id_account`),
  CONSTRAINT `account_dipendente_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `account_dipendente_ibfk_2` FOREIGN KEY (`id_account`) REFERENCES `account` (`id_account`)
);

DROP TABLE IF EXISTS `azienda_cliente`;
CREATE TABLE `azienda_cliente` (
  `id_azienda` int NOT NULL,
  `id_cliente` int NOT NULL,
  PRIMARY KEY (`id_azienda`,`id_cliente`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `azienda_cliente_ibfk_1` FOREIGN KEY (`id_azienda`) REFERENCES `azienda` (`id_azienda`),
  CONSTRAINT `azienda_cliente_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`)
);

DROP TABLE IF EXISTS `commessa_dipendente`;
CREATE TABLE `commessa_dipendente` (
  `id_commessa` int NOT NULL,
  `id_dipendente` int NOT NULL,
  `rate` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id_commessa`,`id_dipendente`),
  KEY `id_dipendente` (`id_dipendente`),
  CONSTRAINT `commessa_dipendente_ibfk_1` FOREIGN KEY (`id_commessa`) REFERENCES `commessa` (`id_commessa`),
  CONSTRAINT `commessa_dipendente_ibfk_2` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`)
);

DROP TABLE IF EXISTS `dipendente_azienda`;
CREATE TABLE `dipendente_azienda` (
  `id_dipendente` int NOT NULL,
  `id_azienda` int NOT NULL,
  `data_inizio_rapporto` date NOT NULL,
  `matricola` varchar(45) DEFAULT NULL,
  `data_fine_rapporto` date DEFAULT NULL,
  PRIMARY KEY (`id_dipendente`,`id_azienda`),
  UNIQUE KEY `matricola_UNIQUE` (`matricola`),
  KEY `id_azienda` (`id_azienda`),
  CONSTRAINT `dipendente_azienda_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `dipendente_azienda_ibfk_2` FOREIGN KEY (`id_azienda`) REFERENCES `azienda` (`id_azienda`)
);

DROP TABLE IF EXISTS `saltini`;
CREATE TABLE `saltini` (
  `id_account` int NOT NULL auto_increment,
  `salt` char(64) NOT NULL,
  PRIMARY KEY (`id_account`),
  KEY `id_account` (`id_account`),
  CONSTRAINT `saltini_ibfk_1` FOREIGN KEY (`id_account`) REFERENCES `account` (`id_account`)
);


INSERT INTO `tipoContratto`(nome_tipocontratto, descrizione) VALUES ('indeterminato',NULL);

INSERT INTO `dipendente` VALUES (1,'bruno','rossi','123','696', 1,'brunorossi@gmail.com','1234');

INSERT INTO `tipoAccount`(nome_id_tipoAccount, lista_funzioni_del_profilo) VALUES ('administrator','admin'),('dipendente','user');

INSERT INTO `account` VALUES (1,'bruno','pop',0, 1),(2,'mario','mem',1, 2);

INSERT INTO `commessa` VALUES (1, null, 1, 1, '2022-01-01', '2022-03-30');

INSERT INTO `tipoPresenza`(nome_id_tipoPresenza, perc_maggiorazione_paga_oraria, paga_oraria) VALUES ('orario standard',0,NULL),('assenza',0,NULL),('festivo',30,NULL),('malattia',0,NULL);

INSERT INTO `presenza` VALUES (1,'2022-01-01', 3,1,50);

INSERT INTO `account_dipendente` VALUES (1, 1);

INSERT INTO `azienda_cliente` VALUES (1, 1);

INSERT into `commessa_dipendente` VALUES (1, 1, 200);

INSERT INTO `dipendente_azienda` VALUES (1, 1, '2022-01-01', '000', '2022-05-05');
