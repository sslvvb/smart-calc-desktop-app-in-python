// Modules to control application life and create native browser window
const { app, BrowserWindow } = require('electron')
const path = require('path')
const { spawn } = require('child_process');
const axios = require('axios');
const fs = require('fs');
const { execFile } = require('child_process');

const FIX_PATH = '/Users/hjerilyn/Desktop/fix.txt';

fs.appendFile(FIX_PATH, app.getAppPath() + '\n', (err) => {
  if (err) {
    console.error('Error appending to file:', err);
  } else {
    console.log('Line appended to file successfully.');
  }
});

function createWindow() {
  console.log("start createWindow");
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })
  // mainWindow.webContents.openDevTools()

  const appPath = app.getAppPath(); // Get the absolute path of the Electron app.
  // const projectPath = path.join(appPath, 'project'); // Construct the absolute path to the 'project' folder.
  // const subpy = spawn('python3', ['manage.py', 'runserver'], {
  //   cwd: projectPath // Set the working directory for the child process to the 'project' folder.
  // });

  // const projectPath = path.join(__dirname, 'project');
  // const projectPath = path.join('/Users/sslvvb/Documents/S21/Projects/Python/python_calc_3/my_git_rep_python_calc/src/dist/mac-arm64/python_calc.app/Contents/Resources/app/project');
  // process.chdir(projectPath); // Change the working directory to the project folder.
  // const subpy = spawn('python3', ['manage.py', 'runserver']);

  // Ваш код для выполнения execFile с параметрами
  const filePath = path.join(appPath, 'project', 'dist', 'smart_calc', 'smart_calc');
  fs.appendFile(FIX_PATH, filePath + '\n', (err) => {
    if (err) {
      console.error('Error appending to file:', err);
    } else {
      console.log('Line appended to file successfully.');
    }
  });
  const args = ['runserver', 'localhost:8000', '--noreload'];
  execFile(filePath, args, (error, stdout, stderr) => {
    if (error) {
      console.error(`Ошибка при выполнении: ${error.message}`);
      fs.appendFile(FIX_PATH, `Ошибка при выполнении: ${error.message}` + '\n', (err) => {
        if (err) {
          console.error('Error appending to file:', err);
        } else {
          console.log('Line appended to file successfully.');
        }
      });
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });

  fs.appendFile(FIX_PATH, 'start django' + '\n', (err) => {
    if (err) {
      console.error('Error appending to file:', err);
    } else {
      console.log('Line appended to file successfully.');
    }
  });

  setTimeout(() => {
    console.log("start load url");
    mainWindow.loadURL('http://127.0.0.1:8000');

    fs.appendFile(FIX_PATH, 'done url' + '\n', (err) => {
      if (err) {
        console.error('Error appending to file:', err);
      } else {
        console.log('Line appended to file successfully.');
      }
    });

  }, 15000);
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
