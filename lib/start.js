(function() {
  'use strict';

  var shell = require('shelljs');
  var path = require('path');
  var nconf = require('nconf');
  var childProcess = require('child_process');
  var configFile = path.join(process.env.npm_config_quichean_nconf_path,
    'pytools', 'config.json');
  var user = process.env.npm_package_config_user;
  var cpOptions = {};
  var cmd = 'python ' + path.join(__dirname, 'service.py');
  var venvPath;
  var uid;
  var gid;

  nconf.file({file: configFile});
  venvPath = nconf.get('virtualenvs:path');
  //shell.exec('sudo -u ' + user + ' whoami');
  //shell.exec('su ' + user);
  //console.log('switched user');
  //shell.exec('whoami');
  uid = Number(shell.exec('id -u ' + user, {silent: true}).output);
  gid = Number(shell.exec('id -g ' + user, {silent: true}).output);
  cpOptions['uid'] = uid;
  cpOptions['gid'] = gid;
  console.log('uid: ' + uid + ', gid: ' + gid);
  //childProcess.spawn(cmd, cpOptions);
  //childProcess.spawn(cmd);
  shell.exec('python ' + path.join(__dirname, 'service.py'));
})();
