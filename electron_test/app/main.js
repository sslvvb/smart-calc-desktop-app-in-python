// // Modules to control application life and create native browser window
// const { app, BrowserWindow } = require('electron')
// const path = require('path')

// const { spawn } = require('child_process');

// let pythonProcess;

// // Event handler for a button click
// function handleClick() {
//   // Spawn the Python process if it's not already running
//   if (!pythonProcess) {
//     pythonProcess = spawn('python', ['path/to/your/python_script.py']);

//     // Listen for data from the Python process
//     pythonProcess.stdout.on('data', (data) => {
//       // Handle the response from the Python process
//       console.log(`Received data from Python: ${data}`);
//     });
//   }

//   // Send a message to the Python process
//   pythonProcess.stdin.write('Hello from Electron!');
//   pythonProcess.stdin.end();
// }


// function createWindow() {
//   // Create the browser window.
//   const mainWindow = new BrowserWindow({
//     width: 800,
//     height: 600,
//     webPreferences: {
//       preload: path.join(__dirname, 'preload.js')
//     }
//   })

//   // and load the index.html of the app.
//   mainWindow.loadFile('index.html')

//   // Open the DevTools.
//   mainWindow.webContents.openDevTools()
// }

// // This method will be called when Electron has finished
// // initialization and is ready to create browser windows.
// // Some APIs can only be used after this event occurs.
// app.whenReady().then(() => {
//   createWindow()

//   app.on('activate', function () {
//     // On macOS it's common to re-create a window in the app when the
//     // dock icon is clicked and there are no other windows open.
//     if (BrowserWindow.getAllWindows().length === 0) createWindow()
//   })
// })

// // Quit when all windows are closed, except on macOS. There, it's common
// // for applications and their menu bar to stay active until the user quits
// // explicitly with Cmd + Q.
// app.on('window-all-closed', function () {
//   if (process.platform !== 'darwin') app.quit()
// })

// // In this file you can include the rest of your app's specific main process
// // code. You can also put them in separate files and require them here.







const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

// Get the absolute path to the Python script
// const pythonScriptPath = path.join(__dirname, 'reverse_text.py');
// const pythonInterpreter = '/opt/goinfre/hjerilyn/homebrew/bin/python3';

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  mainWindow.loadFile('index.html');
  // mainWindow.loadURL('http://localhost:5000/test');

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  mainWindow.webContents.openDevTools()

  let backend;
  backend = path.join(process.cwd(), '../build/app_exe/reverse_text')
  var execfile = require('child_process').execFile;
  execfile(
    backend,
    {
      windowsHide: true,
    },
    (err, stdout, stderr) => {
      if (err) {
        console.log(err);
      }
      if (stdout) {
        console.log(stdout);
      }
      if (stderr) {
        console.log(stderr);
      }
    }
  )
}

// app.on('ready', createWindow);
app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  const { exec } = require('child_process');
  exec('taskkill / f / t / im app_exe/reverse_text', (err, stdout, stderr) => {
    if (err) {
      console.log(err)
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.log(`stderr: ${stderr}`);
  });
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});


// ipcMain.on('reverse-text', (event, text) => {
//   console.log('Received text:', text);

//   const appPath = app.getAppPath();
//   const pythonScriptPath = path.join(appPath, 'python', 'reverse_text.py');
//   const pythonProcess = spawn('python3', [pythonScriptPath, text]);

//   pythonProcess.stdout.on('data', (data) => {
//     const reversedText = data.toString().trim(); // конвертирует вывод в строку без пробелов
//     console.log('Reversed text:', reversedText); // 
//     event.reply('reversed-text', reversedText); // перевернутый текст отправляется обратно во фронтенд
//   });

//   pythonProcess.stderr.on('data', (data) => {
//     console.error('Python error:', data.toString());
//   });

//   pythonProcess.on('close', (code) => {
//     console.log('Python process exited with code:', code);
//   });

//   pythonProcess.stdin.write(text);
//   pythonProcess.stdin.end();
// });
