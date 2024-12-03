#! /usr/bin/bash

NOM=UNO

DIR_WRK=$PWD

DIR_LOG=$DIR_WRK/Log
FIC_LOG=$DIR_LOG/$(basename $0 .sh).$NOM.log
[ -d $DIR_LOG ] || mkdir -p $DIR_LOG

exec > >(tee $FIC_LOG) 2>&1

PRM=true
ENT=true
REC=true
EVA=true

DIR_GUI=$DIR_WRK/Gui
GUI_ENT=$DIR_GUI/train.gui
GUI_DEV=$DIR_GUI/devel.gui

DIR_SEN=$DIR_WRK/Sen
DIR_PRM=$DIR_WRK/Prm/$NOM
DIR_REC=$DIR_WRK/Rec/$NOM

FIC_MOD=$DIR_WRK/Mod/$NOM.mod
[ -d $(dirname $FIC_MOD) ] || mkdir -p $(dirname $FIC_MOD)

LIS_MOD=$DIR_WRK/Lis/vocales.lis

FIC_RES=$DIR_WRK/Res/$NOM.res
[ -d $(dirname $FIC_RES) ] || mkdir -p $(dirname $FIC_RES)

dirPrm="-p $DIR_PRM"
dirSen="-s $DIR_SEN"
EXEC="parametriza.py $dirSen $dirPrm $GUI_ENT $GUI_DEV"
$PRM && { echo $EXEC && $EXEC || exit 1; }

dirPrm="-p $DIR_PRM"
dirMar="-m $DIR_SEN"
LisFon="-f $LIS_MOD"
ficMod="-o $FIC_MOD"
EXEC="entrena.py $dirMar $dirPrm $LisFon $ficMod $GUI_ENT"
$ENT && { echo $EXEC && $EXEC || exit 1; }


ficMod="-m $FIC_MOD"
dirRec="-r $DIR_REC"
dirPrm="-p $DIR_PRM"
EXEC="reconoce.py $dirPrm $dirRec $ficMod $GUI_DEV"
$REC && { echo $EXEC && $EXEC || exit 1; }

dirMar="-m $DIR_SEN"
dirRec="-r $DIR_REC"
EXEC="evalua.py $dirMar $dirRec $GUI_DEV"
$EVA && { echo $EXEC && $EXEC | tee $FIC_RES || exit 1; }


hostname
pwd
date
