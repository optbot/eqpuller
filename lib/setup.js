(function() {
  'use strict';

  var pytools = require('@optbot/pytools');
  var shell = require('shelljs');
  var path = require('path');
  var nconf = require('nconf');
  var user = process.env.npm_package_config_user;
  var configFile = path.join(process.env.npm_config_quichean_nconf_path,
    'pytools', 'config.json');
  var venvPath;
  var venvs;

  shell.exec(path.join(__dirname, 'createuser.sh') + ' ' + user + ' "--shell /bin/bash"');
  pytools.init();
  nconf.file({file: configFile});
  venvPath = nconf.get('virtualenvs:path');
  shell.cd(venvPath);
  venvs = shell.ls();
  if (venvs.indexOf(user) < 0) {
    shell.exec('virtualenv ' + user);
    shell.exec('chown root:sudo *');
  }
  else {
    console.log('virtualenv ' + user + ' already exists, updating');
  }
  shell.cd(user);
  shell.cp('-f', path.join(__dirname, 'requirements.txt'), '.');
  shell.exec('pip install -r requirements.txt');    
  shell.exec('chown -R ' + user + ':sudo .');
})();
