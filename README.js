<!DOCTYPE html>
<html>
<head>
    <title>Jogodacobrinha</title>
</head>
<body>
    <canvas id="stage" width="600" height="600"></canvas>
    <script type="text/javascript">
        window.onload = function(){
            
            var stage = document.getElementById('stage');
            var ctx = stage.getContext("2d");
            document.addEventListener("keydown", keyPush);
            setInterval(game, 85); 

            const vel = 1;//quantas casas a cobra vai andar

            var vx = vy = 0; //começa com velocidade zero
            var px = 10;
            var py = 45;
            var tp = 30;
            var qp = 20;
            var ax=ay=15;

            var trail = [];//rastro
            tail = 5;

            function game(){//posição da cabeça da cobra
                px += vx;
                py += vy;

                if (px <0) {
                    px = qp-1;
                }
                if (px > qp-1) {
                    px = 0;
                }
                if (py < 0){
                    py = qp-1;
                }
                if (py > qp-1){
                    py = 0;
                }

                ctx.fillStyle = "black"; //cores do jojo
                ctx.fillRect(0,0, stage.width, stage.height);

                ctx.fillStyle = "red";
                ctx.fillRect(ax*tp, ay*tp, tp,tp);

                ctx.fillStyle = "green";
                for (var i = 0; i < trail.length; i++) {
                    ctx.fillRect(trail[i].x*tp, trail[i].y*tp, tp-1, tp-1);
                     if (trail[i].x == px && trail[i].y == py)
                    {
                        vx = vy=0;
                        tail =5;
                    }
                }
                trail.push({ x:px, y:py })
                while (trail.length > tail) {
                    trail.shift();//tira o primeiro elemento do array
                }
                if (ax==px && ay==py){ //aumenta cauda
                    tail++;
                    setInterval(game, 85) -1; //aqui que ta dando erro 
                    ax = Math.floor(Math.random()*qp);//maça aleatoria
                    ay = Math.floor(Math.random()*qp);

                
                }
            }
            function keyPush(event){//setas de movimento

                switch (event.keyCode) {
                    case 37:
                        vx = -vel;
                        vy = 0;
                        break;
                    case 38:
                        vx = 0;
                        vy = -vel;
                        break;
                    case 39: 
                        vx = vel;
                        vy = 0;
                        break;
                    case 40: 
                        vx = 0;
                        vy = vel;
                        break;
                    default:
                        break;
                }
            }
        }
    </script>
</body>
</html>
