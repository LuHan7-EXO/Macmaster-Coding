$(document).ready(function(){
  var aNote = document.getElementById("aaudio");
  var bNote = document.getElementById("baudio");
  var cNote = document.getElementById("caudio");
  var dNote = document.getElementById("daudio");
  var eNote = document.getElementById("eaudio");
  var fNote = document.getElementById("faudio");

  $("#a").mousedown(function () {
      aNote.currentime = 0;
      aNote.play();

  });

  $("#b").mousedown(function () {
      bNote.currentime = 0;
      bNote.play();

  });

  $("#c").mousedown(function () {
      cNote.currentime = 0;
      cNote.play();

  });

  $("#d").mousedown(function () {
      dNote.currentime = 0;
      dNote.play();

  });
  $("#e").mousedown(function () {
      eNote.currentime = 0;
      eNote.play();

  });
  $("#f").mousedown(function () {
      fNote.currentime = 0;
      fNote.play();

  });



});
