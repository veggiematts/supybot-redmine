Redmine plugin for Supybot/Limnoria
===================================

This Supybot/Limnoria plugin allows to display informations about Redmine issues and direct links to them.

How to install
--------------

The informations are fetched from [Redmine](http://www.redmine.org/) through it's [Rest API](http://www.redmine.org/projects/redmine/wiki/Rest_api), so you will need to install [Restkit](http://benoitc.github.com/restkit/) (package python-restkit on Debian).


How to configure
----------------

It is based on the Mantis/Bugzilla plugins, so it uses the same command and more or less the same configuration variables:

 * urlbase: The base URL for the Redmine instance this plugin will retrieve bug informations from.

 * apikey: Your Redmine API key. The Rest API must be enabled in Redmine in Administration -> Settings -> Authentication. You can then get your API Key on your account page ( /my/account ) when logged in, on the right-hand pane of the default layout.

 * bugMsgFormat: Change the message format for bug details, following tokens will be replaced before being printed: \_ID\_, \_URL\_, \_AUTHOR\_, \_CATEGORY\_, \_SUBJECT\_, \_STATUS\_ .  \_CRLF\_ will split the response in two (or more) lines.

 * bugSnarfer: Determines whether the bug snarfer will be enabled, such that any bug ### seen in the channel will have its information reported into the channel. Channel Specific variable.

 * bugSnarferTimeout: Users often say "RM XXX" several times in a row, in a channel. If "RM XXX" has been said in the last (this many) seconds, don't fetch its data again. If you change the value of this variable, you must reload this plugin for the change to take effect.


How to use
----------

Once the plugin is loaded and (at least) urlbase and apikey are set, you can display informations about a Redmine issue with the "bug #" command, where # is the issue number.
If you enable the bugSnarfer variable for a given channel, you won't need using the "bug" command anymore, just write "RM #", and the bot will automatically display informations about the issue.


Update
------
Get latest version at : https://github.com/veggiematts/supybot-redmine
