"""
Patch subcommands.
"""

import logging
import sys

import arrow
import click

from git_pw import api
from git_pw import utils

LOG = logging.getLogger(__name__)

_list_headers = ('ID', 'Date', 'Name', 'Submitter', 'State', 'Archived',
                 'Delegate')
_sort_fields = ('id', '-id', 'name', '-name', 'date', '-date')


@click.command(name='apply', context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('patch_id', type=click.INT)
@click.option('--series', type=click.INT, metavar='SERIES',
              help='Series to include dependencies from. Defaults to latest.')
@click.option('--deps/--no-deps', default=True,
              help='When applying the patch, include dependencies if '
              'available. Defaults to using the most recent series.')
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
def apply_cmd(patch_id, series, deps, args):
    """Apply patch.

    Apply a patch locally using the 'git-am' command. Any additional ARGS
    provided will be passed to the 'git-am' command.
    """
    LOG.debug('Applying patch: id=%d, series=%s, deps=%r, args=%s', patch_id,
              series, deps, ' '.join(args))

    patch = api.detail('patches', patch_id)

    if deps and not series:
        series = '*'
    elif not deps:
        series = None

    mbox = api.download(patch['mbox'], {'series': series})

    utils.git_am(mbox, args)


@click.command(name='download')
@click.argument('patch_id', type=click.INT)
@click.argument('output', type=click.File('wb'), required=False)
@click.option('--diff', 'fmt', flag_value='diff',
              help='Show patch in diff format.')
@click.option('--mbox', 'fmt', flag_value='mbox', default=True,
              help='Show patch in mbox format.')
def download_cmd(patch_id, output, fmt):
    """Download patch in diff or mbox format.

    Download a patch but do not apply it. ``OUTPUT`` is optional and can be an
    output path or ``-`` to output to ``stdout``. If ``OUTPUT`` is not
    provided, the output path will be automatically chosen.
    """
    LOG.debug('Downloading patch: id=%d, format=%s', patch_id, fmt)

    path = None
    patch = api.detail('patches', patch_id)

    if output:
        if fmt == 'diff':
            content = patch['diff']
        else:
            content = api.get(patch['mbox']).text

        output.write(content)

        if output != sys.stdout:
            path = output.name
    else:
        if fmt == 'diff':
            # TODO(stephenfin): We discard the 'diff' field so we can get the
            # filename and save to the correct file. We should expose this
            # information via the API
            path = api.download(patch['mbox'].replace('mbox', 'raw'))
        else:
            path = api.download(patch['mbox'])

    if path:
        LOG.info('Downloaded patch to %s', path)


def _show_patch(patch, fmt):

    def _format_series(series):
        return '%-4d %s' % (series.get('id'), series.get('name') or '-')

    output = [
        ('ID', patch.get('id')),
        ('Message ID', patch.get('msgid')),
        ('Date', patch.get('date')),
        ('Name', patch.get('name')),
        ('URL', patch.get('web_url')),
        ('Submitter', '%s (%s)' % (patch.get('submitter').get('name'),
                                   patch.get('submitter').get('email'))),
        ('State', patch.get('state')),
        ('Archived', patch.get('archived')),
        ('Project', patch.get('project').get('name')),
        ('Delegate', (patch.get('delegate').get('username')
                      if patch.get('delegate') else '')),
        ('Commit Ref', patch.get('commit_ref'))]

    prefix = 'Series'
    for series in patch.get('series'):
        output.append((prefix, _format_series(series)))
        prefix = ''

    utils.echo(output, ['Property', 'Value'], fmt=fmt)


@click.command(name='show')
@utils.format_options
@click.argument('patch_id', type=click.INT)
def show_cmd(fmt, patch_id):
    """Show information about patch.

    Retrieve Patchwork metadata for a patch.
    """
    LOG.debug('Showing patch: id=%d', patch_id)

    patch = api.detail('patches', patch_id)

    _show_patch(patch, fmt)


@click.command(name='update')
@click.argument('patch_ids', type=click.INT, nargs=-1, required=True)
@click.option('--commit-ref', metavar='COMMIT_REF',
              help='Set the patch commit reference hash')
@click.option('--state', metavar='STATE',
              help='Set the patch state. Should be a slugified representation '
              'of a state. The available states are instance dependant.')
@click.option('--delegate', metavar='DELEGATE',
              help='Set the patch delegate. Should be unique user identifier: '
              'either a username or a user\'s email address.')
@click.option('--archived', metavar='ARCHIVED', type=click.BOOL,
              help='Set the patch archived state.')
@utils.format_options
def update_cmd(patch_ids, commit_ref, state, delegate, archived, fmt):
    """Update one or more patches.

    Updates one or more Patches on the Patchwork instance. Some operations may
    require admin or maintainer permissions.
    """
    for patch_id in patch_ids:
        LOG.debug('Updating patch: id=%d, commit_ref=%s, state=%s, '
                  'archived=%s', patch_id, commit_ref, state, archived)

        if delegate:
            users = api.index('users', [('q', delegate)])
            if len(users) == 0:
                LOG.error('No matching delegates found: %s', delegate)
                sys.exit(1)
            elif len(users) > 1:
                LOG.error('More than one delegate found: %s', delegate)
                sys.exit(1)

            delegate = users[0]['id']

        data = []
        for key, value in [('commit_ref', commit_ref), ('state', state),
                           ('archived', archived), ('delegate', delegate)]:
            if value is None:
                continue

            data.append((key, value))

        patch = api.update('patches', patch_id, data)

        _show_patch(patch, fmt)


@click.command(name='list')
@click.option('--state', metavar='STATE', multiple=True,
              default=['under-review', 'new'],
              help='Show only patches matching these states. Should be '
              'slugified representations of states. The available states '
              'are instance dependant.')
@click.option('--submitter', metavar='SUBMITTER', multiple=True,
              help='Show only patches by these submitters. Should be an '
              'email, name or ID.')
@click.option('--delegate', metavar='DELEGATE', multiple=True,
              help='Show only patches by these delegates. Should be an '
              'email or username.')
@click.option('--archived', default=False, is_flag=True,
              help='Include patches that are archived.')
@utils.pagination_options(sort_fields=_sort_fields, default_sort='-date')
@utils.format_options(headers=_list_headers)
@click.argument('name', required=False)
@api.validate_multiple_filter_support
def list_cmd(state, submitter, delegate, archived, limit, page, sort, fmt,
             headers, name):
    """List patches.

    List patches on the Patchwork instance.
    """
    LOG.debug('List patches: states=%s, submitters=%s, delegates=%s, '
              'archived=%r', ','.join(state), ','.join(submitter),
              ','.join(delegate), archived)

    params = []

    for state in state:
        params.append(('state', state))

    for subm in submitter:
        # we support server-side filtering by email (but not name) in 1.1
        if (api.version() >= (1, 1) and '@' in subm) or subm.isdigit():
            params.append(('submitter', subm))
        else:
            params.extend(api.retrieve_filter_ids('people', 'submitter', subm))

    for delg in delegate:
        # we support server-side filtering by username (but not email) in 1.1
        if (api.version() >= (1, 1) and '@' not in delg) or delg.isdigit():
            params.append(('delegate', delg))
        else:
            params.extend(api.retrieve_filter_ids('users', 'delegate', delg))

    params.extend([
        ('q', name),
        ('archived', 'true' if archived else 'false'),
        ('page', page),
        ('per_page', limit),
        ('order', sort),
    ])

    patches = api.index('patches', params)

    # Format and print output

    output = []

    for patch in patches:
        item = [
            patch.get('id'),
            arrow.get(patch.get('date')).humanize(),
            utils.trim(patch.get('name')),
            '%s (%s)' % (patch.get('submitter').get('name'),
                         patch.get('submitter').get('email')),
            patch.get('state'),
            'yes' if patch.get('archived') else 'no',
            (patch.get('delegate') or {}).get('username', ''),
        ]

        output.append([])
        for idx, header in enumerate(_list_headers):
            if header not in headers:
                continue

            output[-1].append(item[idx])

    utils.echo_via_pager(output, headers, fmt=fmt)
