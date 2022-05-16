#Brad Dai Salazar Leal
do{
    $opc = Read-Host -Prompt "[1] Ver Status Perfi [2] Cambiar Status Perfi [3] Ver Perfil Red Actual [4] Cambiar Perfil Red Actual [5] Ver Reglas Bloqueo [6] Agregar Reglas Bloqueo [7]Eliminar Reglas Bloqueo [8] salir "
    switch($opc){
        1 {
            Ver-StatusPerfil

        } 2 {
            Cambiar-StatusPerfi

        } 3 {
            Ver-PerfilRedActual

        } 4 {
            Cambiar-PerfilRedActual

        } 5 {
            Ver-ReglasBloqueo

        } 6 {
            Agregar-ReglasBloqueo

        } 7 {
            Eliminar-ReglasBloqueo
        } 8 {
            Write-Host 'Estas saliendo'
        }
    }
}while ($opc -ne 8)
