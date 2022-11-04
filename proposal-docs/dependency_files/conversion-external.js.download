/*
 * Author: Instapage.com
 * Credits: Carl Hartl https://github.com/carhartl/jquery-cookie/blob/master/jquery.cookie.js
 * License: MIT
 * Version: 1.1
 */

function InstapageExternalConversion( page, variation )
{
	var c;

	var Cookie = function()
	{
		var pluses = /\+/g;

		this.decode = function(s)
		{
			try
			{
				// If we can't decode the cookie, ignore it, it's unusable.
				return decodeURIComponent(s.replace(pluses, ' '));
			}
			catch(e)
			{
			}
		};

		this.decodeAndParse = function(s)
		{
			if (s.indexOf('"') === 0)
			{
				// This is a quoted cookie as according to RFC2068, unescape...
				s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
			}

			s = this.decode(s);

			return s;
		};

		this.get = function cookie( key )
		{
			var result = false;
			var i;
			var parts;
			var name;
			var cookie;
			// To prevent the for loop in the first place assign an empty array
			// in case there are no cookies at all. Also prevents odd result when
			// calling $.cookie().
			var cookies = document.cookie ? document.cookie.split('; ') : [];

			for( i = 0, l = cookies.length; i < l; i++)
			{
				parts = cookies[i].split('=');
				name = this.decode(parts.shift());
				cookie = parts.join('=');

				if ( key && key === name )
				{
					result = this.decodeAndParse(cookie);
					break;
				}

				// Prevent storing a cookie that we couldn't decode.
				if (!key && (cookie = this.decodeAndParse(cookie)) !== undefined) {
					result[name] = cookie;
				}
			}

			return result;
		};

		this.set = function( key, value )
		{
			var d = new Date();
			var expires;

			d.setTime( d.getTime() + ( 7 * 24 * 60 * 60 * 1000) );
			expires = "expires=" + d.toUTCString();
			document.cookie = key + "=" + value + "; " + expires + "; path=/";
		};
	};

	var reportConversion = function( data )
	{
		var image = new Image();
		var image_src = ( data && data.external_image ) ? data.external_image : ( "//app.instapage.com/ajax/stats/conversion-pixel/"+ page + "/" + variation + "/transparent.png" );

		if( !data.variation )
		{
			data.variation = 'A';
		}

		function successSend()
		{
			window.InstapageLocalStorage.conversionDataSent( data );
		}

		image.onload = successSend;
		image.src = image_src;
	};

	var loadScript = function( script_src, callback)
	{
		var head = document.getElementsByTagName( 'head' )[ 0 ];
		var script = document.createElement( 'script' );
		script.type = 'text/javascript';
		script.src = script_src;

		// most browsers
		script.onload = callback;

		// IE 6 & 7
		script.onreadystatechange = function()
		{
			if( this.readyState === 'complete' )
			{
				callback();
			}
		};
		head.appendChild( script );
	};

	// we have to know which page we convert
	if( !page )
	{
		return;
	}

	var addSnowplowScript = function( data ) {
		;(function(p,l,o,w,i,n,g){if(!p[i]){p.GlobalSnowplowNamespace=p.GlobalSnowplowNamespace||[];
		p.GlobalSnowplowNamespace.push(i);p[i]=function(){(p[i].q=p[i].q||[]).push(arguments)
		};p[i].q=p[i].q||[];n=l.createElement(o);g=l.getElementsByTagName(o)[0];n.async=1;
		n.src=w;g.parentNode.insertBefore(n,g)}}(window,document,"script",data.snowplow_url,"instapageSp"));
		;(function(i,n,s,t,a,p,g){i[a]||(i[a]=function(){(i[a].q=i[a].q||[]).push(arguments)},
		i[a].q=i[a].q||[],p=n.createElement(s),g=n.getElementsByTagName(s)[0],p.async=1,
		p.src=t,g.parentNode.insertBefore(p,g))}(window,document,"script",data.snowplow_wrapper_url,"_instapageSnowplow"));

		try {
			window._instapageSnowplow( 'setWrapperConfig', {
				lpContext: {
					lp_id: data.page_id,
					lp_variation_id: data.variation_id,
					lp_version: data.version,
					subaccount_id: data.customer_id
				},
				namespace: 'instapage-external'
			} );
			window._instapageSnowplow( 'trackExternalConversion', 'instapage-external' );
		} catch ( e ) {
			console.warn( 'Snowplow tracker error', e );
		}
	}

	loadScript( '//storage.googleapis.com/instapage-assets/server-storage-local.js', function()
	{
		loadScript( '//instapage-scripts.s3.amazonaws.com/jstorage.js', function()
		{
			c = new Cookie();

			if( typeof ServerStorageLocal === 'function' )
			{
				window.InstapageLocalStorage = new ServerStorageLocal();

				window.InstapageLocalStorage.getConversionData( page, function( data )
				{
					if( data )
					{
						if( data.timestamp_sent && data.timestamp_sent > Date.now() - ( 7 * 24 * 60 * 60 * 1000 ) )
						{
							return;
						}

						reportConversion( data );

						if( data.snowplow_url && data.snowplow_wrapper_url ) {
							addSnowplowScript( data )
						}
					}
				} );
			}

		} );
	} );

}
