var data = {
  includes: [],
  complete: [],
  inventory: {}
};
var nodecounter = 0;

/**
 * Helper function for avoiding callback hell
 * 
 * @param {any} fns 
 */
function chain(fns) {
  fn = fns.shift()
  if(fn) {
    fn(() => chain(fns));
  }
}

function getCSV(callback){
  $.ajax('rsinclude.csv', {
    type: 'GET',
    success: function( res ) { 
      rows =  res.split('\n');
      // Pop off the header
      rows.shift();
      rows.forEach(element => {
        data['includes'].push(element.split(','))
      });
      console.log("done getting csv");
      callback();
    },
    error:function(e){ 
      console.log('ERROR: Lambda returned error\n\n' + e.responseText);
      spinnerStop();
    },      
  });  
}

function getJSON(callback){
  $.ajax('inventory.json', {
    type: 'GET',
    success: function( res ) { 
      data.inventory = res
      console.log("done getting json");
      callback();
    },
    error:function(e){ 
      console.log('ERROR: Lambda returned error\n\n' + e.responseText);
      spinnerStop();
    },      
  });    
}

function spinnerStart(callback) {
  console.log('starting spinner')
  var spinner = new Spinner().spin();
  $('body').append(spinner.el);
  callback();
}
function spinnerStop(callback) {
  $('body .spinner').remove();
  console.log("stopping spinner")
  callback();
}

function processData(callback){
  data.tree = {}  
  data.prodTree = {}
  // first let's process a completeness tree
  data.includes.forEach(el => {
    // Only show the things that should be here
    if (el[1] == 1) {
      // Do we have a project for it?
      var present = data.inventory[el[0] + "/project.rs.xml"] ? true: false;
      var currlevel = data.tree;

      // Now accumulate presence / absence tree
      var keyparts = el[0].split("/");
      keyparts.forEach((keypart,idx) => {
        if (!currlevel[keypart]){
          currlevel[keypart] = { name: keypart, present: 0, projects: 0}
          if (idx == keyparts.length -1){
            currlevel[keypart].path = keyparts;
          }
          else{
            currlevel[keypart].children = {}
          }
        }
        if (present) currlevel[keypart].present +=1;

        if (idx < keyparts.length -1){
          currlevel[keypart].projects +=1;
          currlevel = currlevel[keypart].children;
        }
      });
    }
  });
  // Now do it again for the product tree with a slight difference
  data.includes.forEach(el => {
    // Only show the things that should be here
    if (el[1] == 1) {
      // Do we have a project for it?
      var present = data.inventory[el[0] + "/project.rs.xml"] ? true: false;
      var currlevel = data.prodTree;

      // Now accumulate presence / absence tree
      var keyparts = el[0].split("/");
      var prod = keyparts[keyparts.length -1];
      if (!currlevel[prod]){
        currlevel[prod] = { name: prod, children: {}, present: 0, projects: 0}
      }

      currlevel[prod].projects += 1;
      currlevel[prod].present += present ? 1:0
      currlevel = currlevel[prod].children;

      currlevel[el[0]] = { 
        name: el[0], 
        present: present ? 1:0, 
        projects: 1,
        path: keyparts
      }

    }
  });
  console.log('done processing data');
  callback();
}

/**
 * Helper function to kick off our recursion and clean up after
 * 
 * @param {any} callback 
 */
function renderTreeStart(callback){
  renderTree($('#inventory'), data.tree);
  renderTree($('#inventorytype'), data.prodTree); 
  console.log("done rendering tree");
  callback();
}

/**
 * Our recursive tree walker
 * 
 * @param {any} $node 
 * @param {any} treenodes 
 */
function renderTree($ulnode, treenodes) {
  for (var tnid in treenodes) {
    if (treenodes.hasOwnProperty(tnid)) {
      nodecounter++;
      var $li = $('<li class="accordion-item" data-accordion-item>');
      var titleString = tnid;
      var $a = $('<a href="#tnid'+nodecounter+'" class="accordion-title grid-x">');
      $('<span class="title">'+titleString+'</span>').appendTo($a);

      if (treenodes[tnid].children){
        var donestring = "( " + treenodes[tnid].present + " / " +treenodes[tnid].projects + " )";
        var percent = (100*(parseInt(treenodes[tnid].present) / parseFloat(treenodes[tnid].projects))).toFixed(0);
        $('<span class="donenum">'+donestring+'</span>').appendTo($a);
        $('<span class="percentdone">'+percent +'%</span>').appendTo($a);        
      }
      var $body = $('<div class="accordion-content" data-tab-content id="tnid'+nodecounter+'">');

      $a.appendTo($li);
      $body.appendTo($li);
      $li.appendTo($ulnode);

      // This is a branch
      if (treenodes[tnid].children){
        $li.addClass("branch");
        $ul = $('<ul class="accordion" data-nodename="'+tnid+'">')
        $ul.appendTo($body);
        renderTree($ul, treenodes[tnid].children);      
      }
      // This is a leaf (product)
      else{
        $li.addClass("product");
        if (treenodes[tnid].present){
          $li.addClass("present");
          var xmlpath = treenodes[tnid].path.join("/") + "/project.rs.xml";
          meta = data.inventory[xmlpath].meta;
          $table = $('<table class="metatable table">');
          $table.appendTo($body);
          for (var key in meta) {
            if (meta.hasOwnProperty(key)) {
              $row = $('<tr>');
              $key = $('<td class="metaname">'+key+'</td>');
              $val = $('<td class="metaval">'+meta[key]+'</td>')
              $key.appendTo($row);
              $val.appendTo($row);
              $row.appendTo($table);
            }
          }
        }
        else{
          $li.addClass("absent");
        }
      }
    }
  }
}


function renderTreeProducts($ulnode, treenodes) {
  for (var tnid in treenodes) {
    if (treenodes.hasOwnProperty(tnid)) {
      nodecounter++;
      var $li = $('<li class="accordion-item" data-accordion-item>');
      var titleString = tnid;
      var $a = $('<a href="#tnid'+nodecounter+'" class="accordion-title grid-x">');
      $('<span class="title">'+titleString+'</span>').appendTo($a);

      if (treenodes[tnid].children){
        var donestring = "( " + treenodes[tnid].present + " / " +treenodes[tnid].projects + " )";
        var percent = (100*(parseInt(treenodes[tnid].present) / parseFloat(treenodes[tnid].projects))).toFixed(0);
        $('<span class="donenum">'+donestring+'</span>').appendTo($a);
        $('<span class="percentdone">'+percent +'%</span>').appendTo($a);        
      }
      var $body = $('<div class="accordion-content" data-tab-content id="tnid'+nodecounter+'">');

      $a.appendTo($li);
      $body.appendTo($li);
      $li.appendTo($ulnode);

      // This is a branch
      if (treenodes[tnid].children){
        $li.addClass("branch");
        $ul = $('<ul class="accordion" data-nodename="'+tnid+'">')
        $ul.appendTo($body);
        renderTree($ul, treenodes[tnid].children);      
      }
      // This is a leaf (product)
      else{
        $li.addClass("product");
        if (treenodes[tnid].present){
          $li.addClass("present");
          var xmlpath = treenodes[tnid].path.join("/") + "/project.rs.xml";
          meta = data.inventory[xmlpath].meta;
          $table = $('<table class="metatable table">');
          $table.appendTo($body);
          for (var key in meta) {
            if (meta.hasOwnProperty(key)) {
              $row = $('<tr>');
              $key = $('<td class="metaname">'+key+'</td>');
              $val = $('<td class="metaval">'+meta[key]+'</td>')
              $key.appendTo($row);
              $val.appendTo($row);
              $row.appendTo($table);
            }
          }
        }
        else{
          $li.addClass("absent");
        }
      }
    }
  }
}

function Inventory(){
  // var elem = new Foundation.OffCanvas($('#offCanvas'));
  var finalize = function(callback){
    var options = {
      allowAllClosed: true,
      deepLink: false,
      deepLinkSmudge: false,
      deepLinkSmudgeDelay: 300,
      multiExpand: true,
      slideSpeed: 250,
      updateHistory: false    
    }
    $('.accordion').each((key, el) => {
      var elem = new Foundation.Accordion($(el), options);
    })
    $(document).foundation();  
    callback();
  }
  chain([spinnerStart, getCSV, getJSON, processData, renderTreeStart, finalize, spinnerStop]);

};

