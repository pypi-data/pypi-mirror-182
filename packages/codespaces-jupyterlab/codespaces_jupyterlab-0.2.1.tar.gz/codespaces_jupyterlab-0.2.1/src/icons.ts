import vmSvgstr from '../icons/vm.svg';
import bookSvgstr from '../icons/book.svg';
import watchSvgstr from '../icons/watch.svg';
import repoSvgstr from '../icons/repo.svg';
import tagSvgstr from '../icons/tag.svg';
import historySvgstr from '../icons/history.svg';
import sourceControlSvgstr from '../icons/source-control.svg';
import { LabIcon } from '@jupyterlab/ui-components';

export const createdIcon = new LabIcon({
    name: 'created',
    svgstr: bookSvgstr
  });
  
  export const timeoutIcon = new LabIcon({
    name: 'timeout',
    svgstr: watchSvgstr
  });
  
  export const repoIcon = new LabIcon({
    name: 'repo',
    svgstr: repoSvgstr
  });
  
  export const sourceControlIcon = new LabIcon({
    name: 'source-control',
    svgstr: sourceControlSvgstr
  });
  
  export const codespaceNameIcon = new LabIcon({
    name: 'codespaceName',
    svgstr: tagSvgstr
  });
  
  export const machineIcon = new LabIcon({
    name: 'machine-details',
    svgstr: vmSvgstr
  });
  
  export const retentionIcon = new LabIcon({
    name: 'retention-period',
    svgstr: historySvgstr
  });