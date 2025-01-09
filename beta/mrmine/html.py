global start_cap, end_cap
start_cap=r'''
<!DOCTYPE html>
<html>
    <head>
        <style>
            red {
                font-family: 'Trebuchet MS';
                color: rgb(200, 0, 0);
            }
            yellow {
                font-family: 'Trebuchet MS';
                color: rgb(200, 200, 0);
            }
            green {
                font-family: 'Trebuchet MS';
                color: rgb(0, 200, 0);
            }
            cyan {
                font-family: 'Trebuchet MS';
                color: rgb(0, 200, 200);
            }
            blue {
                font-family: 'Trebuchet MS';
                color: rgb(0, 0, 200);
            }
            purple {
                font-family: 'Trebuchet MS';
                color: rgb(200, 0, 200);
            }
            white {
                font-family: 'Trebuchet MS';
                color: rgb(255, 255, 255);
            }
            black {
                font-family: 'Trebuchet MS';
                color: rgb(0, 0, 0);
            }
            gray {
                font-family: 'Trebuchet MS';
                color: rgb(100, 100, 100);
            }
            xs {
                font-family: 'Trebuchet MS';
                font-size: 10px;
            }
            sm {
                font-family: 'Trebuchet MS';
                font-size: 20px;
            }
            m {
                font-family: 'Trebuchet MS';
                font-size: 30px;
            }
            l {
                font-family: 'Trebuchet MS';
                font-size: 40px;
            }
            xl {
                font-family: 'Trebuchet MS';
                font-size: 50px;
            }
            normal {
                font-family: 'Trebuchet MS';
                font-size: 30px;
                color: rgb(255, 255, 255)
            }
        </style>
        <!-- <s> = strikethrough -->
        <!-- <b> = bold -->
        <!-- <u> = underline -->
        <!-- <i> = italic -->
        <!-- <bx/> = new line -->
    </head>
    <body>'''
sell=r'''
        <sell>
            <xl>Selling Post</xl><br>
            <button><m><b>Coal</b></m></button><br>
            <button><m><b><orange>Copper</orange></b></m></button><br>
            <button><m><b><gray>Silver</gray></b></m></button><br>
        </sell>'''
craft=r'''
        <craft>
            <xl>Craft an item</xl><br>
        </craft>'''
unknown=r'''
            <button onclick="unknown()"><m><b>? ? ?</b></m></button><br>'''
login=r'''
        <form id="loginform" action="/action_page.php">
            Game Key: <input type="text" name="fname" value=""><br>
            Name: <input type="text" name="lname" value=""><br><br>
        </form> 
        <button onclick="getlogindata()">Submit</button>
        <script>
        const fs = require('fs');
        function getlogindata() {
            var data = document.getElementById("loginform");
            fs.writeFile('V/workspaces/coolmathgames/v1.5-alpha.3/mrmine/htmldata.txt', data.join(''));
        }
        </script>'''
end_cap=r'''
    </body>
</html>'''
def writehtml(spec, code):
    with open('v1.5-alpha.3/mrmine/index.html', 'w') as htmlfile:
        htmlfile.writelines(start_cap)
        if spec==0:
            htmlfile.writelines(login)
        elif spec==1:
            htmlfile.writelines(sell)
        elif spec==2:
            htmlfile.writelines(craft)
        elif spec=='custom':
            htmlfile.writelines(code)
        htmlfile.writelines(end_cap)
def checkhtmldata():
    with open('v2.0-beta/mrmine/htmldata.txt', 'r') as file:
        if file.readlines() != '':
            return file.readlines()
        else:
            return None