#!/bin/bash

echo "Content-type: text/html"
echo

echo "<html>"
echo "<head>"
echo "<meta charset=UTF-8>"
echo "</head>"
echo "<body>"

  echo "<form method=GET action=\"${SCRIPT}\">"\
       '<table nowrap>'\
          '<tr><td>1st val:</TD><TD><input type="text" name="val_x" size=12></td></tr>'\
          '<tr><td>2nd val:</td><td><input type="text" name="val_y" size=12 value=""></td>'\
          '</tr></table>'
  echo '<br><input type="submit" value="Calcular"><br>'

  if [ -z "$QUERY_STRING" ]; then
        exit 0
  else
     X=`echo "$QUERY_STRING" | sed -n 's/^.*val_x=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     Y=`echo "$QUERY_STRING" | sed -n 's/^.*val_y=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     Z=$(($X+$Y))
     echo "<br>TOTAL: "$Z
  fi

echo "</body>"
echo "</html>"
