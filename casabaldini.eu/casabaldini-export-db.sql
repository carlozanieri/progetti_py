--
-- File generated with SQLiteStudio v3.4.15 on ven gen 24 00:28:13 2025
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: beb_menuweb
CREATE TABLE IF NOT EXISTS "beb_menuweb" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "codice" varchar(20) NOT NULL, "radice" varchar(20) NOT NULL, "livello" integer NOT NULL, "titolo" varchar(64) NOT NULL, "descrizione" varchar(256) NOT NULL, "link" varchar(512) NOT NULL, "attivo" integer NOT NULL, "icon" varchar(255) NOT NULL, "workplace" integer NOT NULL, "param1" varchar(255) NOT NULL, "ordine" integer NOT NULL);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (1, 'archiviopost', 'archivio', 3, 'Archivio Post', 'archivio post', '/archive', 0, 'ui-icon-document', 402220600, 'pub', 1);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (2, 'generale', 'generale', 1, 'MENU Generale', 'Menu Generale', '', 0, '/icone/home', 0, 'pub', 2);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (3, 'turismo', 'turismo', 2, 'Turismo', 'Percorsi', '', 1, 'ui-icon-document', 402218601, 'pub', 2);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (4, 'manifesta', 'generale', 2, 'manifestazioni', 'manifestazioni', '/manifestazioni', 0, 'ui-icon-document', 402220600, 'pub', 3);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (5, 'territorio', 'territorio', 2, 'Territorio', 'Territorio', '', 1, 'ui-icon-document', 402221400, 'pub', 4);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (6, 'home', 'home', 2, 'Home', 'home', '', 0, 'ui-icon-document', 402221400, 'pub', 28);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (7, 'sanpiero', 'territorio', 3, 'San Piero a Sieve', 'San Piero a Sieve', '/sanpiero', 1, 'ui-icon-document', 402220600, 'pub', 5);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (8, 'conferenza', 'contatti', 3, 'conferenza', 'Multi Conferenza', '/conferenza/', 1, 'ui-icon-document', 402220600, 'priv', 6);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (9, 'percorsi', 'turismo', 3, 'Percorsi Trekking ', 'Percorsi', '/percorsi', 1, 'ui-icon-document', 402218601, 'priv', 2);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (10, 'mugello', 'territorio', 3, 'Prestige', 'Prestige', '/mugello', 1, 'ui-icon-document', 402220600, 'pub', 7);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (11, 'contatti', 'contattist', 3, 'Contatti e numeri utili', 'contatti e numeri utili', '/contatti', 1, 'ui-icon-document', 402220600, 'pub', 8);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (12, 'contattist', 'contatti', 2, 'Contatti e Stampa', 'Contatti e Stampa', '', 0, 'ui-icon-document', 402220600, 'pub', 9);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (13, 'arrivare', 'arrivare', 2, 'Come Arrivare', 'Come Arrivare', '/arrivare', 1, 'ui-icon-document', 402220600, 'pub', 10);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (14, 'blog', 'home', 3, 'BLOG', 'Blog', '/blog?pag=blog', 1, 'ui-icon-document', 402220600, 'pub', 11);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (15, 'logout', 'logout', 3, 'logout', 'logout', 'qApp.quit', 1, 'ui-icon-document', 402220600, 'pub', 12);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (16, 'anelli', 'turismo', 3, 'Gli Anelli dell''Infinito', 'gli anelli dell''infinito', '/infinito', 1, 'ui-icon-document', 402221400, 'pub', 13);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (17, 'monumenti', 'turismo', 3, 'Monumenti', 'Monumenti', '/monumenti', 1, 'ui-icon-document', 402221400, 'pub', 14);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (18, 'gastronomia', 'turismo', 3, 'Gastronomia', 'Gastronomia', '/gastronomia', 1, 'ui-icon-document', 402220600, 'pub', 15);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (19, 'report', 'report', 2, 'REPORT', 'REPORT', '/Report', 1, 'ui-icon-document', 402221400, 'pub', 16);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (20, 'chisiamo', 'chisiamo', 2, 'Chi Siamo', 'Chi Siamo', '/chisiamo', 1, 'ui-icon-document', 402220400, 'pub', 17);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (21, 'chisiamo', 'chisiamo', 3, 'Chi Siamo', 'Chi Siamo', '/chisiamo', 1, 'ui-icon-document', 402220400, 'pub', 18);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (22, 'streaming', 'contatti', 3, 'View Streaming', 'View streaming', '/selectviewstreaming/', 1, 'ui-icon-document', 402220600, 'pub', 19);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (23, 'serverstream', 'contatti', 3, 'ServerStreaming', 'Server streaming', '/selectstreaming/', 1, 'ui-icon-document', 402220600, 'priv', 20);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (24, 'mangiare', 'turismo', 3, 'Dove Mangiare', 'Dove Mangiare', '/mangiare', 1, 'ui-icon-document', 402221400, 'pub', 21);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (25, 'dormire', 'turismo', 3, 'Dove Dormire', 'Dove Dormire', '/dormire', 1, 'ui-icon-document', 402221400, 'pub', 22);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (26, 'login', 'home', 3, 'Login', 'Login', '/login', 1, 'ui-icon-document', 402221400, 'pub', 23);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (27, 'logout', 'home', 3, 'logout', 'logout', 'logout', 1, 'ui-icon-document', 402221400, 'pub', 24);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (28, 'admin', 'admin', 2, 'Amministrazione', 'Amministrazione', 'admin', 1, 'ui-icon-document', 402221400, 'priv', 25);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (29, 'insmanif', 'admin', 3, 'Inserisce Manifestazione', 'Inserisce Manifestazione', '/ins_manifestazioni', 1, 'ui-icon-document', 402221400, 'priv', 26);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (30, 'home', 'home', 2, 'Home', 'home', '/blog', 0, 'ui-icon-document', 402221400, 'pub', 27);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (31, 'homeh', 'home', 3, 'HomE', 'home', '', 0, 'ui-icon-document', 402221400, 'pub', 28);
INSERT INTO beb_menuweb (id, codice, radice, livello, titolo, descrizione, link, attivo, icon, workplace, param1, ordine) VALUES (32, 'cart', 'home', 3, 'CART', 'Cart', '/cart', 1, 'ui-icon-document', 402220600, 'pub', 2);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
