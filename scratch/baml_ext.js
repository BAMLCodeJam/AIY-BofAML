/**
BoAML AI Scratch 2.0 extension
Please save in /usr/lib/scratch2/scratch_extensions

*/
(function (ext) {

    var socket = null;
    var recognised = false;
    var onButton = false;
    var connected = false;

    // an array to hold possible digital input values for the reporter block
    var digital_inputs = new Array(32);
    var myStatus = 1; // initially yellow
    var myMsg = 'not_ready';

    ext.cnct = function (callback) {
        window.socket = new WebSocket("ws://127.0.0.1:9000");
        window.socket.onopen = function () {
            var msg = JSON.stringify({
                "command": "ready"
            });
            window.socket.send(msg);
            myStatus = 2;

            // change status light from yellow to green
            myMsg = 'ready';
            connected = true;

            // initialize the reporter buffer
            digital_inputs.fill('0');

            // give the connection time establish
            window.setTimeout(function() {
            callback();
        }, 1000);

        };

        window.socket.onmessage = function (message) {
            var msg = JSON.parse(message.data);
            if ('onButton' in msg) {
	      onButton = msg['onButton'];
            }
            console.log(message.data);
	    console.log(msg);
        };

        window.socket.onclose = function (e) {
            console.log("Connection closed.");
            socket = null;
            connected = false;
            myStatus = 1;
            myMsg = 'not_ready'
        };
    };

    // Cleanup function when the extension is unloaded
    ext._shutdown = function () {
        var msg = JSON.stringify({
            "command": "shutdown"
        });
        window.socket.send(msg);
    };
    
    ext.turnOn = function (callback) {
        if (connected == false) {
            alert("Server Not Connected");
        }
        // validate the pin number for the mode
        var msg = JSON.stringify({
            "command": "turnOn",
        });
        console.log(msg);
        window.socket.send(msg);
    };
    
    ext.turnOff = function (callback) {
        if (connected == false) {
            alert("Server Not Connected");
        }
        // validate the pin number for the mode
        var msg = JSON.stringify({
            "command": "turnOff",
        });
        console.log(msg);
        window.socket.send(msg);
    };


    // when the say  block is executed
    ext.say = function (text) {
        if (connected == false) {
            alert("Server Not Connected");
        }
        // validate the pin number for the mode
        var msg = JSON.stringify({
            "command": "say", "text": text
        });
        console.log(msg);
        window.socket.send(msg);
        
    };

    // when the say in a different lang block is executed
    ext.sayLang = function (text, lang) {
        if (connected == false) {
            alert("Server Not Connected");
        }
        // validate the pin number for the mode
        var msg = JSON.stringify({
            "command": "sayLang", "text": text, "lang": lang
        });
        console.log(msg);
        window.socket.send(msg);
        
    };
    
    // Status reporting code (icon in scratch)
    ext._getStatus = function (status, msg) {
        return {status: myStatus, msg: myMsg};
    };

    ext.recognise = function(text){
        if (connected == false) {
            alert("Server Not Connected");
        }
        // validate the pin number for the mode
        var msg = JSON.stringify({
            "command": "recognise", "text": text
        });
        console.log(msg);
        window.socket.send(msg);
    };

    ext.recogniseFct = function(){
	if (recognised == true){
		return true;
	}	
	return false;
    };

   ext.onButtonFn = function(){
	if (onButton == true){
	  onButton = false;
	  return true;
	}	
	return false;
    };

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            // Block type, block name, function name
            ["w", 'Connect to AI.', 'cnct'],
            [" ", 'Turn On Light', 'turnOn'],
            [" ", 'Turn Off Light', 'turnOff'],
            [" ", 'Say %s', 'say', "Hello", "message"],
	    ["h", 'When AI button pressed', 'onButtonFn'],
	    [" ", 'Say %s in %m.language', 'sayLang', "Bonjour", "fr"],

        ],
        "menus": {
            "language": ["af","sq","ar","hy","bn","ca","zh","zh-cn","zh-tw","zh-yue","hr","cs","da","nl","en","en-au","en-uk","en-us","eo","fi","fr","de","el","hi","hu","is","id","it","ja","ko","la","lv","mk","no","pl","pt","pt-br","ro","ru","sr","sk","es","es-es","es-us","sw","sv","ta","th","tr","vi","cy"]
	},
        url: 'https://www.bankofamerica.com/'
    };

    // Register the extension
    ScratchExtensions.register('BofAML - AI', descriptor, ext);
})({});

