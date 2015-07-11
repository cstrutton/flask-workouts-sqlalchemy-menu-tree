#!/usr/bin/env python
import os
from app import create_app
from flask.ext.script import Manager, Shell, Server

app = create_app('default')

manager = Manager(app)

# pass any variables you want access to in the shell
def _make_context():
     return dict(app=app)

manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver",
                    Server(host=os.getenv('IP', '0.0.0.0'),
                           port=int(os.getenv('PORT', 5000))))

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
