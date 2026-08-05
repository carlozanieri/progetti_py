INSERT INTO beb_menuweb (codice,radice,livello,titolo,descrizione,link,attivo,icon,workplace,param1,ordine) VALUES
	 ('archiviopost','archivio',3,'Archivio Post','archivio post','/archive',0,'ui-icon-document',402220600,'pub',1),
	 ('generale','generale',1,'MENU Generale','Menu Generale','',0,'/icone/home',0,'pub',2),
	 ('turismo','turismo',2,'Turismo','Percorsi','',1,'ui-icon-document',402218601,'pub',2),
	 ('manifesta','generale',2,'manifestazioni','manifestazioni','/manifestazioni',0,'ui-icon-document',402220600,'pub',3),
	 ('territorio','territorio',2,'Territorio','Territorio','',1,'ui-icon-document',402221400,'pub',4),
	 ('home','home',2,'Home','home','',0,'ui-icon-document',402221400,'pub',28),
	 ('sanpiero','territorio',3,'San Piero a Sieve','San Piero a Sieve','/sanpiero',1,'ui-icon-document',402220600,'pub',5),
	 ('conferenza','contatti',3,'conferenza','Multi Conferenza','/conferenza/',1,'ui-icon-document',402220600,'priv',6),
	 ('percorsi','turismo',3,'Percorsi Trekking ','Percorsi','/percorsi',1,'ui-icon-document',402218601,'priv',2),
	 ('mugello','territorio',3,'Prestige','Prestige','/mugello',1,'ui-icon-document',402220600,'pub',7);
INSERT INTO beb_menuweb (codice,radice,livello,titolo,descrizione,link,attivo,icon,workplace,param1,ordine) VALUES
	 ('contatti','contattist',3,'Contatti e numeri utili','contatti e numeri utili','/contatti',1,'ui-icon-document',402220600,'pub',8),
	 ('contattist','contatti',2,'Contatti e Stampa','Contatti e Stampa','',0,'ui-icon-document',402220600,'pub',9),
	 ('arrivare','arrivare',2,'Come Arrivare','Come Arrivare','/arrivare',1,'ui-icon-document',402220600,'pub',10),
	 ('blog','home',3,'BLOG','Blog','/blog?pag=blog',1,'ui-icon-document',402220600,'pub',11),
	 ('logout','logout',3,'logout','logout','qApp.quit',1,'ui-icon-document',402220600,'pub',12),
	 ('anelli','turismo',3,'Gli Anelli dell''Infinito','gli anelli dell''infinito','/infinito',1,'ui-icon-document',402221400,'pub',13),
	 ('monumenti','turismo',3,'Monumenti','Monumenti','/monumenti',1,'ui-icon-document',402221400,'pub',14),
	 ('gastronomia','turismo',3,'Gastronomia','Gastronomia','/gastronomia',1,'ui-icon-document',402220600,'pub',15),
	 ('report','report',2,'REPORT','REPORT','/Report',1,'ui-icon-document',402221400,'pub',16),
	 ('chisiamo','chisiamo',2,'Chi Siamo','Chi Siamo','/chisiamo',1,'ui-icon-document',402220400,'pub',17);
INSERT INTO beb_menuweb (codice,radice,livello,titolo,descrizione,link,attivo,icon,workplace,param1,ordine) VALUES
	 ('chisiamo','chisiamo',3,'Chi Siamo','Chi Siamo','/chisiamo',1,'ui-icon-document',402220400,'pub',18),
	 ('streaming','contatti',3,'View Streaming','View streaming','/selectviewstreaming/',1,'ui-icon-document',402220600,'pub',19),
	 ('serverstream','contatti',3,'ServerStreaming','Server streaming','/selectstreaming/',1,'ui-icon-document',402220600,'priv',20),
	 ('mangiare','turismo',3,'Dove Mangiare','Dove Mangiare','/mangiare',1,'ui-icon-document',402221400,'pub',21),
	 ('dormire','turismo',3,'Dove Dormire','Dove Dormire','/dormire',1,'ui-icon-document',402221400,'pub',22),
	 ('login','home',3,'Login','Login','/login',1,'ui-icon-document',402221400,'pub',23),
	 ('logout','home',3,'logout','logout','logout',1,'ui-icon-document',402221400,'pub',24),
	 ('admin','admin',2,'Amministrazione','Amministrazione','admin',1,'ui-icon-document',402221400,'priv',25),
	 ('insmanif','admin',3,'Inserisce Manifestazione','Inserisce Manifestazione','/ins_manifestazioni',1,'ui-icon-document',402221400,'priv',26),
	 ('home','home',2,'Home','home','/blog',0,'ui-icon-document',402221400,'pub',27);
INSERT INTO beb_menuweb (codice,radice,livello,titolo,descrizione,link,attivo,icon,workplace,param1,ordine) VALUES
	 ('homeh','home',3,'HomE','home','',0,'ui-icon-document',402221400,'pub',28),
	 ('cart','home',3,'CART','Cart','/cart',1,'ui-icon-document',402220600,'pub',2);
