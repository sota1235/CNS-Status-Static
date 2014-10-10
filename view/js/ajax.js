var Ajax = function(url) {
  this.url = url;
  var self = this;

  // GET時の処理
  this.on_get = null;

  this.get = function() {
    $.ajax(
        {
          url : self.url,
          success : function(data) {
            if(data) {
              if(self.on_get && typeof self.on_get == 'function') self.on_get(data);
            };
          },
          error : function(req, stat, e) {
            setTimeout(self.get, 10000);
          },
          complete : function(e){
          },
          type : 'GET',
          timeout : 60000
        });
  };
};
