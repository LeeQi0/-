<?php
  $charact=$_POST["Channel"];
  $urlLink=$_POST["url"];
  $xml=simplexml_load_file("note.xml") or die("Error: Cannot create object");
  $xml->whether=$charact;
  if($charact=="a")
  {$xml->Channel=}
  if($charact=="b")
  {}
  if($charact=="c")
  {}
  if($charact=="d")
  {}
 if($charact=="e")
  {}
 if($charact=="f")
  {}
  $xml->asXML();
  $myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
  fwrite($myfile, $xml);
  fclose($myfile);

  sleep(15);//sleep 15 sec

  $xml=simplexml_load_file("note.xml") or die("Error: Cannot create object");
  $xml->whether="no";
  $xml->asXML();
  $myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
  fwrite($myfile, $xml);
  fclose($myfile);
 ?>
