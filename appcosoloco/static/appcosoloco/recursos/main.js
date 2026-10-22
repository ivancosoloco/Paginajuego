document.addEventListener('DOMContentLoaded', function () {
    const btnDescargar = document.getElementById('btnDescargar');
    
    if (btnDescargar) {
        btnDescargar.addEventListener('click', function () {
            // Inicializar el modal de Bootstrap
            const modalElement = document.getElementById('modalDescarga');
            const modal = new bootstrap.Modal(modalElement);
            modal.show();

            const barra = document.getElementById('barraProgreso');
            const estado = document.getElementById('estadoDescarga');
            
            // Reiniciar progreso
            barra.style.width = '0%';
            estado.textContent = 'Iniciando servidor de descarga...';

            let progreso = 0;
            const intervalo = setInterval(() => {
                progreso += 25;
                barra.style.width = progreso + '%';

                if (progreso === 50) {
                    estado.textContent = 'Verificando archivos del juego...';
                } else if (progreso === 75) {
                    estado.textContent = 'Comprimiendo paquete (.ZIP)...';
                } else if (progreso >= 100) {
                    clearInterval(intervalo);
                    estado.textContent = '¡Descarga iniciada exitosamente!';
                    
                    // Aquí colocas la ruta real a tu archivo .zip cuando lo subas a static
                    // window.location.href = "/static/appcosoloco/recursos/INFERNO_Game.zip";
                }
            }, 600);
        });
    }
});