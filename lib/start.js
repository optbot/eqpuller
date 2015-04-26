(function() {
  'use strict';

  var shell = require('shelljs');
  var path = require('path');
  var nconf = require('nconf');
  var configFile = path.join(process.env.npm_config_quichean_nconf_path,
    'pytools', 'config.json');
  var user = process.env.npm_package_config_user;
  var venvPath;

  nconf.file({file: configFile});
  venvPath = nconf.get('virtualenvs:path');
  //shell.exec('sudo -u ' + user + ' whoami');
  //shell.exec('su ' + user);
  //console.log('switched user');
  //shell.exec('whoami');
  shell.exec('python ' + path.join(__dirname, 'service.py'));
})();
