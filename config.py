###
# Copyright (c) 2012, Matthias Meusburger
# All rights reserved.
# Based on the Mantis/Bugzilla plugins
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Redmine', True)


Redmine = conf.registerPlugin('Redmine')

conf.registerChannelValue(Redmine, 'bugSnarfer',
    registry.Boolean(False, """Determines whether the bug snarfer will be
    enabled, such that any RM ### seen in the channel
    will have its information reported into the channel."""))

conf.registerGlobalValue(Redmine, 'bugSnarferTimeout',
    registry.PositiveInteger(300, 
    """Users often say "RM XXX" several times in a row, in a channel.
    If "RM XXX" has been said in the last (this many) seconds, don't
    fetch its data again. If you change the value of this variable, you
    must reload this plugin for the change to take effect."""))

conf.registerGlobalValue(Redmine, 'urlbase',
    registry.String('http://www.redmine.org', 
    """The base URL for the Redmine instance this plugin will retrieve
    bug informations from."""))

conf.registerGlobalValue(Redmine, 'bugMsgFormat',
    registry.String('RM _ID_ - _AUTHOR_ - _STATUS_ - _SUBJECT__CRLF__URL_',
    """Change the message format for bug details, following tokens will 
    be replaced before being printed: _ID_, _URL_, _AUTHOR_, 
    _CATEGORY_, _SUBJECT_, _STATUS_ .
    _CRLF_ will split the response in two (or more) lines."""))


conf.registerGlobalValue(Redmine, 'apikey',
    registry.String('', """Your Redmine API key. The Rest API must be enabled
    in Redmine (Administration -> Settings -> Authentication). You can then get
    your API Key on your account page ( /my/account ) when logged in, on the
    right-hand pane of the default layout.""",
                    private=True))



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
