function load_geo() {
        Bokeh.safely(function() {
          (function(root) {
            function embed_document(root) {
var x = document.getElementsByClassName("main-root")[0];
x.setAttribute('id','149fdce1-6e2e-4bc6-babf-c087e9374de3');
x.setAttribute('data-root-id', '15916');
render_items = [{"docid":"d2010126-e9d6-409d-a745-f29f9c88255d","root_ids":["15916"],"roots":{"15916":"149fdce1-6e2e-4bc6-babf-c087e9374de3"}}];
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