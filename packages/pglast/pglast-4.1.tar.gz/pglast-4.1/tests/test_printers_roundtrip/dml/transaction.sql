ABORT

BEGIN

COMMIT

COMMIT PREPARED 'foobar'

PREPARE TRANSACTION 'foobar'

RELEASE SAVEPOINT my_savepoint

ROLLBACK

ROLLBACK PREPARED 'foobar'

ROLLBACK TO SAVEPOINT my_savepoint

SAVEPOINT my_savepoint

START TRANSACTION ISOLATION LEVEL SERIALIZABLE

START TRANSACTION ISOLATION LEVEL SERIALIZABLE, READ ONLY, DEFERRABLE

START TRANSACTION ISOLATION LEVEL READ COMMITTED, READ WRITE, NOT DEFERRABLE
