--
-- File generated with SQLiteStudio v3.4.15 on ven gen 24 01:06:16 2025
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: beb_slider
CREATE TABLE IF NOT EXISTS "beb_slider" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "codice" varchar(24) NOT NULL, "img" varchar(100) NOT NULL, "titolo" varchar(64) NOT NULL, "caption" varchar(512) NOT NULL, "link" varchar(512) NOT NULL);
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (1, 'sanpiero', 'lapieve.jpg', 'La Pieve', 'La Pieve di San Piero a Sieve', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (2, 'sanpiero', 'lapieve.jpg', 'La Pieve', 'La Pieve di San Piero a Sieve', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (3, 'sanpiero', 'lapieve.jpg', 'La Pieve', 'La Pieve di San Piero a Sieve', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (4, 'sanpiero', 'sapiero-storia-provinciale.JPG', 'Via Provinciale', 'La via Provinciale attraversa l''intero paese', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (5, 'mugello', 'lagobilancino.jpg', 'Il Lago di Bilancino', 'Il lago di Bilancino situato nel comune di Barberino di Mugello', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (6, 'mugello', 'montesenario.jpg', 'Monte Giovi', 'Il Monte Giovi (nome originario "Monte di Giove") è un complesso montuoso formato da territori della media montagna. Si trova nella provincia di Firenze ed è posto sui prolungamenti della dorsale appenninica di Monte Morello e Monte Senario, dorsale che separa il Mugello dal Valdarno e dalla bassa Val di Sieve. Rappresenta la parte più orientale di detta dorsale ed è delimitato a nord dall''alta', 'https://it.wikipedia.org/wiki/Monte_Giovi');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (7, 'mugello', 'montegiovi.jpg', 'Santuario di Montesenario', 'Il santuario di Monte Senario è uno dei più importanti santuari della Toscana e si trova sulla collina omonima a nord della città di Firenze, nel comune di Vaglia. Nel dicembre 1917 papa Benedetto XV lo elevò al rango di basilica minore.[1]
', 'https://it.wikipedia.org/wiki/Santuario_di_Montesenario');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (8, 'index', 'trenodellabefana-92.jpg', 'Il Treno Della Befana', 'Ogni anno il treno a vapore  della Befana arriva puntuale alla Stazione Di San Piero', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (9, 'index', 'estemporanea92.jpg', 'Estemporanea di Pittura', 'Estemporanea di Pittura', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (10, 'index', 'mercanzie-in-piazza-92.jpg', 'Mercanzie in Piazza', 'Mercanzie in Piazza', 'https://it.wikipedia.org/wiki/Santuario_di_Montesenario');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (11, 'index', 'ingorgosonoro-92.jpg', 'Ingorgo Sonoro', 'Maratona Musicale famosa in tutta Italia', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (12, 'index', 'simposio-92.jpg', 'Simposio di Scultura', 'Simposio di Scultura', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (13, 'sanpiero', 'stazione.jpg', 'La Stazione', 'La Stazione Ferroviaria di San Piero', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (14, 'sanpiero', 'stazione2.jpg', 'Ai Binari', 'La Stazione vista dal treno.', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');
INSERT INTO beb_slider (id, codice, img, titolo, caption, link) VALUES (15, 'sanpiero', 'lapieve.jpg', 'La Pieve', 'La Pieve di San Piero a Sieve', 'https://it.wikipedia.org/wiki/Lago_di_Bilancino');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
