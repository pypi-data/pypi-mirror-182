"use strict";
(self["webpackChunkjupyterlab_copy_relative_path"] = self["webpackChunkjupyterlab_copy_relative_path"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const application_1 = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
const filebrowser_1 = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
const docmanager_1 = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
const apputils_1 = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
const ui_components_1 = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
const utils_1 = __webpack_require__(/*! ./utils */ "./lib/utils.js");
const algorithm_1 = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
const extension = {
    id: 'context-menu',
    autoStart: true,
    requires: [filebrowser_1.IFileBrowserFactory, docmanager_1.IDocumentManager, application_1.ILabShell],
    activate: (app, factory, docManager, labShell) => {
        // For File Browser items
        app.commands.addCommand('filebrowser:copy-relative-path', {
            label: 'Copy Relative Path',
            caption: 'Copy path relative to the active document.',
            icon: ui_components_1.fileIcon.bindprops({ stylesheet: 'menuItem' }),
            execute: () => {
                const widget = factory.tracker.currentWidget;
                if (!widget) {
                    return;
                }
                const item = widget.selectedItems().next();
                if (!item) {
                    return;
                }
                if (!labShell.currentWidget) {
                    return;
                }
                console.debug('labShell.currentWidget:', labShell.currentWidget);
                const context = docManager.contextForWidget(labShell.currentWidget);
                if (!context) {
                    return;
                }
                console.debug(`context.path: ${context.path}`);
                console.debug(`item.path: ${item.path}`);
                const relativePath = utils_1.getRelativePath(item.path, context.path);
                console.debug(`Copied relative path to clipboard: ${relativePath}`);
                apputils_1.Clipboard.copyToSystem(relativePath);
            },
            isVisible: () => !!factory.tracker.currentWidget &&
                !!factory.tracker.currentWidget.selectedItems().next() &&
                !!labShell.currentWidget &&
                !!docManager.contextForWidget(labShell.currentWidget),
        });
        // [NOTE] borrowed from jupyterlab/packages/application-extension/src/index.tsx
        const { shell } = app;
        const contextMenuWidget = () => {
            const test = (node) => !!node.dataset.id;
            const node = app.contextMenuHitTest(test);
            if (!node) {
                // Fall back to active widget if path cannot be obtained from event.
                return shell.currentWidget;
            }
            return (algorithm_1.find(shell.widgets('main'), widget => widget.id === node.dataset.id) ||
                shell.currentWidget);
        };
        // For tabs
        app.commands.addCommand('docmanager:copy-relative-path', {
            label: 'Copy Relative Path',
            caption: 'Copy path relative to the active document',
            icon: ui_components_1.fileIcon.bindprops({ stylesheet: 'menuItem' }),
            execute: () => {
                const targetWidget = contextMenuWidget();
                if (!targetWidget) {
                    return;
                }
                console.debug('widget:', targetWidget);
                const targetContext = docManager.contextForWidget(targetWidget);
                if (!targetContext) {
                    return;
                }
                if (!labShell.currentWidget) {
                    return;
                }
                console.debug('labShell.currentWidget:', labShell.currentWidget);
                const currentContext = docManager.contextForWidget(labShell.currentWidget);
                if (!currentContext) {
                    return;
                }
                console.debug(`(current) context.path: ${currentContext.path}`);
                console.debug(`(target)  context.path: ${targetContext.path}`);
                const relativePath = utils_1.getRelativePath(targetContext.path, currentContext.path);
                console.debug(`Copied relative path to clipboard: ${relativePath}`);
                apputils_1.Clipboard.copyToSystem(relativePath);
            },
            isVisible: () => !!labShell.currentWidget &&
                !!docManager.contextForWidget(labShell.currentWidget),
        });
    },
};
exports["default"] = extension;


/***/ }),

/***/ "./lib/utils.js":
/*!**********************!*\
  !*** ./lib/utils.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.getRelativePath = void 0;
// Get relative path of target with respect to reference
const getRelativePath = (target, reference) => {
    const xs = target.split('/');
    const ys = reference.split('/').slice(0, -1);
    const n = Math.min(xs.length, ys.length);
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (xs[i] === ys[i]) {
            count++;
        }
        else {
            break;
        }
    }
    const numUps = ys.length - count;
    const zs = [...Array(numUps).fill('..'), ...xs.slice(count)];
    return zs.join('/');
};
exports.getRelativePath = getRelativePath;


/***/ })

}]);
//# sourceMappingURL=lib_index_js.259bbf260a96c66e38a3.js.map