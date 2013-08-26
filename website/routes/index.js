
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.hello = function(req, res){
  res.send('Time is ' + new Date().toString());
};

exports.wait = function(req, res){
  var url_str = req.body['url'];
  res.render('wait', { url: url_str });
  //call python to retrieve image
  var cmd = '/home/ubuntu/webshot/src/ScreenShotTest.py \"' + url_str + '\"'

  var sys = require('sys')
  var exec = require('child_process').exec;
  var child;
 
  console.log("run command: " + cmd)

  child = exec(cmd, function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error);
    }

    //redirect with file name to another page
    var img_path = stdout;

    console.log('image saved to ' + img_path);

    //res.render('view', { image: 'snapshots/snapshot.png', url: url_str});
  });
  

};

exports.view = function(req, res){
    res.render('view', { image: 'snapshots/snapshot.png', url: req.body['url']});
  //res.render('view', { image: 'snapshots/snapshot.png'});
};

