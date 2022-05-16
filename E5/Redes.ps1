#Brad Dai Salazar Leal
do{
    $opc = Read-Host -Prompt "[1] Ver Perfil Red Actual [2] Cambiar Perfil Red Actual [3] salir "
    switch($opc){
          1 {
            Ver-PerfilRedActual

        } 2 {
            Cambiar-PerfilRedActual

        } 3 {
            Write-Host 'Estas saliendo'
        }
    }
}while ($opc -ne 3)
