# Periscope Dashboard Migration Tool
`version: 0.1.1`

This tool is to ease migration of Sisense/Periscope dashboards from old to new spaces over the course of the 2022 migration.
- Old spaces - `2ND`, `INSTACASH`
- New spaces - `GENERAL`, `PRODUCT`, `PRIVATE`

## Docs
Confluence - Periscope Migration: Dashboard Cloning
- Refer to this document for a more detailed step-by-step guide on using this tool and other FAQs

## Quickstart
#### Step 1: Clone locally
```shell
git clone git@github.com:MoneyLion/de-miscellaneous.git
cd de-miscellaneous/tools/periscope_dashboard_space_migration
```

#### Step 2: Setup and initialisation
```shell
make init
```
-   Creates virtual environment
-   Installs requirements

#### Step 3: Activate virtual environment
```shell
source env/bin/activate
```

#### Step 4: Run the app
```shell
make run
```

Running the app will show the following messages and open a new browser window.
```shell
Running app...

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168...:8501
```

If a new browser window does not open for you, click on one of the URL links from your terminal, or copy and paste the address `http://localhost:8501` into your browser’s address bar to open the app.


#### Optional: Run app in debug mode
To view all logs, run the app in debug mode.
```shell
make run-debug
```

#### Terminate
Press `CTRL + C` to terminate app.
