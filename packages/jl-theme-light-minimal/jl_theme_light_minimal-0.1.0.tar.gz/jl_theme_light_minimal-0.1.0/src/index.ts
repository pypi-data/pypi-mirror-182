import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';

/**
 * Initialization data for the jl-theme-light-minimal extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jl-theme-light-minimal:plugin',
  autoStart: true,
  requires: [IThemeManager],
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    console.log('JupyterLab extension jl-theme-light-minimal is activated!');
    const style = 'jl-theme-light-minimal/index.css';

    manager.register({
      name: 'jl-theme-light-minimal',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default plugin;
