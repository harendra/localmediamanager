function MediaFinderView() {
	this.initialize = function() {
    	function loaddropdown(){
    		$('.dropdown-toggle').dropdown();
    	}
    	addDirectories();
    	
		imagenumber = "few";
		
		var currentfolder=rootfoldersfile[0];
		rootdirectory=rootfoldersfile[0];
		data=allfiles;
		selectDirectory(currentfolder);
		
		$('#folder').change(function(){
			var selecteddir=$('#folder').find(":selected").text();
			rootdirectory=selecteddir;
			selecteddir=$.trim(selecteddir);
			selectDirectory(selecteddir);
		});
		
		$('#imagenumber').change(function(){
			var selected=$.trim($('#imagenumber').find(":selected").text());
			if(selected=="Fewer Thumbnails"){
				imagenumber="few";
				
			}
			else if(selected=="More Thumbnails"){
				imagenumber="more";
			}
			console.log(imagenumber);
			
			
			var filename = $('.active').attr("foldername");			
			selectDirectory(filename);			
		});

		$('.history').click(function() {
			showHistory();
		});
		createTags();
		
		$('.searchbutton').click(function(){
			search($('.searchtext').val());
		});
		
		$('.searchtext').keypress(function(e) {
        if(e.which == 13) {
        	e.preventDefault();
            jQuery(this).blur();
            search($('.searchtext').val());
        }
    	});
    	
    	$('.brand').click(function(){
    		selectDirectory(currentfolder);
    	});
	}
	
	function search(keyword){		
		$('#folders').empty();
		$('#videosmain').empty();
		var images = new Array();
		var directories = new Array();
		var videos = new Array();	
		for(key in data){
			var currentrootdir=key;
			var currentfilelist=data[key][key]['filelist'];
			for(var i=0;i<currentfilelist.length;i++){
				if(currentfilelist[i].toLowerCase().indexOf(keyword.toLowerCase())!=-1){
					try {
						var currentobj = data[currentrootdir][currentfilelist[i]];
						currentobj['filename'] = currentfilelist[i];
						if (currentobj['type'] == 'file') {
							if (currentobj['filetype'] == 'image') {
								images.push(currentobj);
							} else if (currentobj['filetype'] == 'video') {
								videos.push(currentobj);
							}
						} else if (currentobj['type'] == 'directory') {
							directories.push(currentobj);
						}
					} catch(err) {
		
					}
			
				}
			}
			
		}		
		addFolders(directories);
		addVideos(videos);
	}
	
	function addDirectories(){
		for(var i=0;i<rootfoldersfile.length;i++){
			var current=rootfoldersfile[i];
			var folder=$('<option></option>');
			folder.text(current);
			$('#folder').append(folder);
		}
	}
	function selectDirectory(directory) {
		$('.active').attr("foldername", directory);
		$('.active').unbind('click');
		$('.active').click(function() {
			var currentfolder = $('.active').attr("foldername");
			var i = currentfolder;
			var k = i.split("\\");
			var last = k[k.length - 1];
			var newstr = i.slice(0, i.length - last.length - 1);
			$('.active').attr("foldername", newstr);
			renderPage(newstr);
		});
		renderPage(directory);
	}

	function renderPage(directoryname) {		
		$('#folders').empty();
		$('#videosmain').empty();
		var filenames = data[rootdirectory][directoryname]['filelist'];
		var images = new Array();
		var directories = new Array();
		var videos = new Array();
		for (var i = 0; i < filenames.length; i++) {
			try {
				var currentobj = data[rootdirectory][filenames[i]];
				currentobj['filename'] = filenames[i];
				if (currentobj['type'] == 'file') {
					if (currentobj['filetype'] == 'image') {
						images.push(currentobj);
					} else if (currentobj['filetype'] == 'video') {
						videos.push(currentobj);
					}
				} else if (currentobj['type'] == 'directory') {
					directories.push(currentobj);
				}
			} catch(err) {

			}

		}
		addFolders(directories);
		addVideos(videos);
		//addPhotos(images);
		manageNavigation(directoryname);

	}

	function getFolder(foldername) {
		var folderstr = $('<div class="foldercontainer floatleft"><div class="folders block"><img class="folderimg" src="../assets/img/download.jpg"></div><div class="foldertext block">foldername</div></div>');
		folderstr.find('.foldertext').text(foldername);
		folderstr.click(function() {
			renderPage(foldername)
		});
		return folderstr;
	}

	function addFolders(foldernames) {
		for (var i = 0; i < foldernames.length; i++) {
			var folderstr = getFolder(foldernames[i]['filename']);
			$('#folders').append(folderstr);
		}
	}

	function showHistory() {
		var historyframe="<!doctype html>"+
			"<html lang='en'> "+
			"<head> "+
			"  <meta charset='utf-8' /> "+
			"  <style>#selectable li { border:1px solid #000000;margin:5px;padding:5px;background:#a0a0a0;color:black}</style>"+
			"</head> "+
			"<body>"

		historyframe+='<ol id="selectable">';
		var history = JSON.parse(localStorage['history']);
		for (var i = history.length-1; i >=0; i--) {
			historyframe += '<li  class="ui-widget-content">' + history[i]['date']+":"+history[i]['filename'] + "</li>";
		}
		historyframe += "</ol></body></html>";
		myWindow = window.open('', '', 'width=800,height=700');
		myWindow.document.write(historyframe);
		myWindow.focus();

	}

	function getVideoFrame(filename) {
		var vframe = $('<div class="videosection block"><div class="block"><div class="title block"></div></div><div class="imagecontainer block"></div></div><div class="line" /></div>');
		vframe.find('.title').click(function() {
			var date=new Date();
			if (localStorage['history'] == null) {
				localStorage['history'] = JSON.stringify([{filename:filename,date:date.getFullYear()+"/"+date.getMonth()+1+"/"+date.getDate()}]);
			}else {
				var history = JSON.parse(localStorage['history']);
				history.push({filename:filename,date:date.getFullYear()+"/"+(parseInt(date.getMonth())+1)+"/"+date.getDate()});
				localStorage['history'] = JSON.stringify(history);
			}
			/*
			var videocode = '<video controls><source id="video" src="' + convertToFirefoxPath(filename) + '" type="video/mp4"></source></video>';
			myWindow = window.open('', '', 'width=1000,height=700');
			myWindow.document.write(videocode);
			myWindow.focus();
			*/
		});
		return vframe;
	}

	function addVideos(videonames) {
		for (var i = 0; i < videonames.length; i++) {
			var currentvideo = videonames[i];
			var videoframe = getVideoFrame(currentvideo['filename']);
			videoframe.find('.title').append('<a href="'+currentvideo['filename']+'">'+currentvideo['filename']+'</a>');
			var images = currentvideo['filelist'];
			console.log(imagenumber);
			if (imagenumber == "few") {
				images = [images[1], images[10], images[16]];
			}
			for (var j = 0; j < images.length; j++) {
				var currentimage = images[j];
				var currentimageframe = $('<div class="img"><div class="image"><img class="imgmain" src="" width="auto" height="300"></div>');
				currentimageframe.find('.imgmain').attr('src', convertToFirefoxPath(currentimage));
				videoframe.find('.imagecontainer').append(currentimageframe);
			}
			$('#videosmain').append(videoframe);
		}
	}

	function addPhotos(photos) {

	}

	function createTags() {
		var maxtags=150;
		var tagscount=maxtags;
		if(tags.length<maxtags){
			tagscount=tags.length;
		}
		for (var i = 0; i < tagscount; i++) {
			var tag = $('<div class="tag"></div>');
			tag.text(tags[i]);
			$('#tags').append(tag);
		}

		$('.tag').click(function() {
			var text = $.trim($(this).text());
			search(text);
		});
	}

	function manageNavigation(foldername) {
		$('.active').attr("foldername", foldername);
	}

	function convertToFirefoxPath(path) {
		path = path.replace(/\\/g, "/");
		return "../../" + path;
	}

}
