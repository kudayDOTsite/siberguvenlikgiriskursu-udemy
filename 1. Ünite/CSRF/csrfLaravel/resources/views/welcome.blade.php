<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
       
    </head>
    <body>
     
     <form action="/" method="post">
     {{ csrf_field() }}
        <input type="text" name="isim">
        <input type="text" name="soyisim">
        <input type="submit" value="tamam">
     </form>

    </body>
</html>
