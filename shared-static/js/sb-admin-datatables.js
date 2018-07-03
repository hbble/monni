// Call the dataTables jQuery plugin
$(document).ready(function() {
    $('#expTable, #incTable').dataTable({
      "ordering": false,
      "searching": false
    });
    $('#mixTable').dataTable({
        "ordering": false
    });
  });
