var json_path = "/data.json";
var json_autorefresh_interval = 3;
var json_autorefresh_default = false;
var views = ["welcome", "hosts"];
var views_default = "welcome";

/* utilities *********/

function utils() {}

utils.slugify = function(t) {
  t = t.replace(/[^-a-zA-Z0-9,&\s]+/ig, '');
  t = t.replace(/-/gi, "_");
  t = t.replace(/\s/gi, "-");
  return t;
}

utils.boolicon = function(b) {
  return $('<i class="icon-' + (b ? "ok" : "remove") + '-sign"></i>');
}

/* widgets *********/

function msgbox() {}

msgbox.clear = function() {
  $("#message-box").empty();
}

msgbox.print = function(type, message) {
  this.clear();
  $("#message-box").append('<div class="alert alert-' + type + '"></div>');
  $("#message-box > div").append('<button type="button" class="close" data-dismiss="alert">&times;</button>' + message);
}

function healthbox() {}

healthbox.clear = function() {
  $("#health").empty();
}

healthbox.set = function(val) {
  this.clear();
  $("#health").append(Math.floor(val * 100) + "%");
  $("#health").removeClass("text-success text-error");
  $("#health").addClass("text-" + (val == 1 ? "success" : "error"));
}

/* hosts view management *********/

function hosts_view() {}

hosts_view.collapse_cache = {}

hosts_view.generate_heading = function(slug, hostname)
{
  var heading_link = $('<a class="accordion-toggle" data-toggle="collapse" href="#' + slug + '"></a>');
  heading_link.append('<h5>' + hostname + '</h5>');
  heading_link.click(function() {
    hosts_view.collapse_cache[slug] = !hosts_view.collapse_cache[slug];
  });

  var heading = $('<div class="accordion-heading"></div>');
  heading.append(heading_link);

  return heading;
}

hosts_view.generate_services_table = function(services)
{
  var services_table = $('<table class="table table-bordered table-striped table-condensed"></table>');

  for (var i = 0; i < services.length; ++i) {
    services_table.append(
      $('<tr></tr>').append(
        $('<td></td>').append(
          utils.boolicon(services[i]["up"]).addClass("pull-right"),
          services[i]["name"]
        )
      )
    );
  }

  return services_table.css("margin-bottom", "0");
}

hosts_view.generate_latency_graph = function(latency)
{
  var latency_graph = $('<div class="well"></div>').append(
    Math.ceil(latency),
    " ms latency"
  );

  return latency_graph.css("margin-bottom", "0");
}

hosts_view.generate_body = function(slug, services, latency)
{
  var body = $('<div id="' + slug + '" class="accordion-body collapse"></div>').append(
    $('<div class="row-fluid"></div>').append(
      $('<div class="span6" style="padding: 10px;"></div>').append(
        this.generate_services_table(services)
      ),
      $('<div class="span6" style="padding: 10px;"></div>').append(
        this.generate_latency_graph(latency)
      )
    )
  );

  if (this.collapse_cache[slug])
    body.addClass("in");
  
  return body;
}

/* view management *********/

function views() {}

views.set = function(view) {
  $("[id^=view-]").hide();
  $("#view-" + view).show();
}

views.refresh = function() {
  $("#refresh-button > i").addClass("icon-spin");

  $.ajax({
    url: json_path,
    cache: false,
  }).done(function(res) {
    var data = JSON.parse(res);
    var health = 0;

    $("#view-hosts").empty();

    for (var i = 0; i < data.length; ++i) {
      var host_slug = utils.slugify(data[i]["hostname"]);
      var host_status = data[i]["status"];

      var body = hosts_view.generate_body(host_slug, data[i]["services"], data[i]["latency"]);
      var heading = hosts_view.generate_heading(host_slug, data[i]["hostname"]);
      var group = $('<div class="accordion-group"></div>').append(heading, body);

      heading.addClass(host_status ? 'alert-success' : 'alert-error');
      body.addClass(host_status ? '' : 'in');
      health += (host_status ? 1 : 0);

      $("#view-hosts").append(group);
    }

    healthbox.set(health / data.length);

    msgbox.clear();
  }).fail(function(msg) {
    msgbox.print("error", "Failed to load data.");
  }).complete(function() {
    $("#refresh-button > i").removeClass("icon-spin");
  });
}

/* main *********/

function main() {
  function eventize(f) {
    return function(ev) {
      f(ev);
      return false;
    };
  }

  views.refresh();
  views.set(views_default);

  $("[data-view]").click(eventize(function(ev) { views.set(ev.currentTarget.dataset["view"]); }));

  $("#refresh-button").click(eventize(views.refresh));
  $("#refresh-checkbox").prop("checked", json_autorefresh_default);
  window.setInterval(function() { if ($("#refresh-checkbox").prop("checked")) views.refresh(); }, 1000 * json_autorefresh_interval);
}

$(main);
