# Dashboard de Licitaciones SSR/APR — Hidrogestión

Dashboard estático (HTML/CSS/JS puro, sin dependencias externas) que muestra las licitaciones
de ingeniería SSR/APR detectadas en Mercado Público. Generado automáticamente por el monitoreo
diario de Hidrogestión.

## Contenido de este paquete

- `index.html` — dashboard listo para publicar (datos embebidos, versión vigente al momento de la exportación).
- `dashboard_template.html` — plantilla HTML/CSS/JS (sin datos).
- `dashboard_data_fixed.json` — datos de licitaciones vigentes.
- `regenerar_dashboard.py` — combina la plantilla + los datos y regenera `index.html`.

## 1. Requisitos previos

- Cuenta de [GitHub](https://github.com).
- Cuenta de [Vercel](https://vercel.com) (puede vincularse directamente con la cuenta de GitHub).
- Git instalado localmente.

## 2. Subir el proyecto a GitHub

Desde una terminal, dentro de esta carpeta:

```bash
git init
git add .
git commit -m "Dashboard licitaciones SSR/APR - version inicial"
```

Crea un repositorio nuevo en GitHub (puede ser privado) y luego:

```bash
git remote add origin https://github.com/<tu-usuario>/licitaciones-ssr-dashboard.git
git branch -M main
git push -u origin main
```

## 3. Desplegar en Vercel

1. Entra a [vercel.com/new](https://vercel.com/new).
2. Selecciona "Import Git Repository" y elige el repositorio recién creado.
3. En "Framework Preset" selecciona **Other** (es un sitio estático, no requiere build).
4. Deja "Build Command" y "Output Directory" vacíos (Vercel servirá `index.html` directamente).
5. Haz clic en "Deploy". En ~30 segundos tendrás una URL pública (ej. `licitaciones-ssr-dashboard.vercel.app`).

A partir de este punto, **cada `git push` a la rama `main` dispara un redeploy automático** vía la integración Git de Vercel — esa parte sí es automática una vez configurada.

## 4. Cómo mantenerlo actualizado

Cuando haya licitaciones nuevas (`dashboard_data_fixed.json` actualizado):

```bash
python3 regenerar_dashboard.py
git add index.html dashboard_data_fixed.json
git commit -m "Actualizacion licitaciones $(date +%F)"
git push
```

Vercel redesplegará automáticamente al recibir el push.

## 5. Limitación importante — por qué esto no es 100% automático todavía

El monitoreo diario de licitaciones corre en un entorno Cowork en la nube (sandbox aislado) que
**no tiene acceso de red a `github.com`, `api.github.com` ni `api.vercel.com`** (bloqueados por
política de red del entorno — se verificó explícitamente, no es una suposición). Esto significa
que la tarea programada que detecta licitaciones nuevas **no puede hacer `git push` ni llamar a
la API de Vercel por sí misma**.

En la práctica esto implica:

- La actualización automática y diaria del dashboard sigue funcionando **vía Google Drive**
  (`Dashboard_Licitaciones_SSR.html` en la carpeta del proyecto), que sí se regenera solo cada
  corrida de la tarea programada.
- La versión publicada en Vercel **requiere un paso manual** (o una automatización propia, ej.
  un GitHub Action corriendo en infraestructura de GitHub — que sí tiene acceso a internet sin
  restricciones — programado para leer el JSON desde algún origen accesible y re-publicar).
- Alternativa más simple si se quiere automatización real sin intervención manual: mantener el
  archivo `dashboard_data_fixed.json` (o su equivalente) en un repositorio o storage accesible
  desde GitHub Actions, y que sea ese workflow — no el monitoreo de Mercado Público — el que
  dispare la actualización del repo en cada corrida programada por su lado.

Quedo disponible para ayudar a diseñar esa automatización adicional si se decide perseguirla.
