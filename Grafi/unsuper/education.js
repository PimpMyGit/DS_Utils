function load_education() {
        Bokeh.safely(function() {
          (function(root) {
            function embed_document(root) {
var x = document.getElementsByClassName("main-root")[0];
x.setAttribute('id','1caf8f13-5f32-4b4a-91ee-3a15e2053cee');
x.setAttribute('data-root-id', '10858');
render_items = [{"docid":"ca5a1653-72d1-46f7-9877-463f2ae53125","root_ids":["10858"],"roots":{"10858":"1caf8f13-5f32-4b4a-91ee-3a15e2053cee"}}];
root.Bokeh.embed.embed_items(docs_json, render_items);

            }
            if (root.Bokeh !== undefined) {
              embed_document(root);
            } else {
              var attempts = 0;
              var timer = setInterval(function(root) {
                if (root.Bokeh !== undefined) {
                  clearInterval(timer);
                  embed_document(root);
                } else {
                  attempts++;
                  if (attempts > 100) {
                    clearInterval(timer);
                    console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                  }
                }
              }, 10, root)
            }
          })(window);
        });
    };