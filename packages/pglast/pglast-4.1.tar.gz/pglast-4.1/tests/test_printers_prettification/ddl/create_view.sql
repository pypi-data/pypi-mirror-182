CREATE OR REPLACE VIEW foo AS SELECT a,b FROM bar
=
CREATE OR REPLACE VIEW foo
  AS SELECT a
          , b
     FROM bar
