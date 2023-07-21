// Modules to control application life and create native browser window
const { app, BrowserWindow } = require('electron')
const path = require('path')
const { spawn } = require('child_process');
const axios = require('axios');

async function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })
  mainWindow.webContents.openDevTools()

  // let django=child_process.spawn('python', [__dirname+'/django_folder/start_server.py']); 

  const projectPath = path.join(__dirname, 'project');
  process.chdir(projectPath); // Change the working directory to the project folder.
  const subpy = spawn('python3', ['manage.py', 'runserver']);

  // Listen for the 'error' event to handle any errors during process creation
  subpy.on('error', (err) => {
    console.error('Error starting Django server:', err);
    // Handle the error as appropriate (e.g., show a message, exit the app, etc.)
  });

  // Listen for the 'close' event to handle when the process exits
  subpy.on('close', (code, signal) => {
    console.log(`Django server process exited with code ${code} and signal ${signal}`);
    // Perform any cleanup or handle the process exit as needed
  });

  let isServerReady = false;
  while (!isServerReady) {
    try {
      const response = await axios.get('http://127.0.0.1:8000/server_ready/');
      if (response.data.status === 'ready') {
        isServerReady = true;
        console.log('print before load url');
        mainWindow.loadURL('http://127.0.0.1:8000');
      }
    } catch (error) {
      // If the request fails, wait for a short time before trying again
      await new Promise((resolve) => setTimeout(resolve, 1000)); // Adjust the delay as needed
    }
  }

  // mainWindow.loadURL('http://127.0.0.1:8000');
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
