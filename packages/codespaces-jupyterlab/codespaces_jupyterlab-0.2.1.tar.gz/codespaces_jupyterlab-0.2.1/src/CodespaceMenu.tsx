import { codespaceNameIcon, createdIcon, machineIcon, repoIcon, retentionIcon, sourceControlIcon, timeoutIcon } from './icons';
import { ReactWidget } from '@jupyterlab/apputils';
import React from 'react';

export interface CodespaceData {
  codespace_name: string,
  repo_name: string,
  machine: string,
  git_ref: string,
  git_behind: string,
  git_ahead: string,
  idle_timeout_minutes: string,
  created_ago: string,
  retention_period_days: string
}

class CodespaceMenu extends ReactWidget {
  data: CodespaceData;

  constructor(jsonData: CodespaceData) {
    super();
    this.id = '@jupyterlab-sidepanel/example';
    this.title.iconClass = "codespace-icon jp-SideBar-tabIcon";
    this.title.caption = "Codespace Panel";
    this.data = jsonData;
  }

  render(): JSX.Element {
    return (
      <div className="jp-CodespaceInfo">
        <header>GITHUB CODESPACES</header>
        <ul className="jp-CodespaceInfo-content">
          <li>
            <repoIcon.react className="jp-InfoIcon"/>
            <span>{this.data.repo_name}</span>
          </li>
          <li>
            <codespaceNameIcon.react className="jp-InfoIcon"/>
            <span>{this.data.codespace_name}</span>
          </li>
          <li>
            <sourceControlIcon.react className="jp-InfoIcon"/>
            <span>{this.data.git_ref} • {this.data.git_behind}↓ {this.data.git_ahead}↑</span>
          </li>
          <li>
            <machineIcon.react className="jp-InfoIcon"/>
            <span>{this.data.machine}</span>
          </li>
          <li>
            <timeoutIcon.react className="jp-InfoIcon"/>
            <span>Idle timeout {this.data.idle_timeout_minutes} minutes</span>
          </li>
          <li>
            <createdIcon.react className="jp-InfoIcon"/>
            <span>{this.data.created_ago}</span>
          </li>
          <li>
            <retentionIcon.react className="jp-InfoIcon"/>
            <span>Retention period {this.data.retention_period_days} days</span>
          </li>
        </ul>
      </div>
    );
  }
}

export { CodespaceMenu };