from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import csv

#Obtener tabla de partidos de octavos del contenido de wikipedia

html = """<!DOCTYPE html>
<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available" lang="es" dir="ltr">
<head>
<meta charset="UTF-8">
<title>Anexo:Octavos de final de la Liga de Campeones de la UEFA 2019-20 - Wikipedia, la enciclopedia libre</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available";var cookie=document.cookie.match(/(?:^|; )eswikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":[",\t."," \t,"],
"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],"wgRequestId":"95cd7ecf-c572-4a57-a7a1-3ef5b54675a7","wgCanonicalNamespace":"Anexo","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":104,"wgPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20","wgTitle":"Octavos de final de la Liga de Campeones de la UEFA 2019-20","wgCurRevisionId":154476111,"wgRevisionId":154476111,"wgArticleId":9207107,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Liga de Campeones de la UEFA 2019-20"],"wgPageViewLanguage":"es","wgPageContentLanguage":"es","wgPageContentModel":"wikitext","wgRelevantPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20","wgRelevantArticleId":9207107,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,
"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoticeProject":"wikipedia","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsFlags":6,"wgVisualEditor":{"pageLanguageCode":"es","pageLanguageDir":"ltr","pageVariantFallbacks":"es"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":true,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":50000,"wgULSCurrentAutonym":"español","wgCentralAuthMobileDomain":false,"wgEditSubmitButtonLabelPublish":true,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,"wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgCheckUserClientHintsHeadersJsApi":["architecture","bitness","brands","fullVersionList","mobile","model","platform","platformVersion"],"GEHomepageSuggestedEditsEnableTopics":true,"wgGETopicsMatchModeEnabled":true,"wgGEStructuredTaskRejectionReasonTextInputEnabled":false,"wgGELevelingUpEnabledForUser":false};RLSTATE={
"skins.vector.user.styles":"ready","ext.gadget.imagenesinfobox":"ready","ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","skins.vector.user":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.cite.styles":"ready","codex-search-styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","wikibase.client.init":"ready","ext.wikimediaBadges":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","mediawiki.toggleAllCollapsibles","site","mediawiki.page.ready","mediawiki.toc","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.a-commons-directo","ext.gadget.ReferenceTooltips","ext.gadget.refToolbar","ext.gadget.switcher","ext.urlShortener.toolbar","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init",
"ext.visualEditor.targetLoader","ext.echo.centralauth","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.cx.uls.quick.actions","ext.checkUser.clientHints"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
}];});});</script>
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=codex-search-styles%7Cext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cskins.vector.icons%2Cstyles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector-2022">
<script async="" src="/w/load.php?lang=es&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector-2022"></script>
<meta name="ResourceLoaderDynamicStyles" content="">
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=ext.gadget.imagenesinfobox&amp;only=styles&amp;skin=vector-2022">
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=site.styles&amp;only=styles&amp;skin=vector-2022">
<noscript><link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=noscript&amp;only=styles&amp;skin=vector-2022"></noscript>
<meta name="generator" content="MediaWiki 1.42.0-wmf.17">
<meta name="referrer" content="origin">
<meta name="referrer" content="origin-when-cross-origin">
<meta name="robots" content="max-image-preview:standard">
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=1000">
<meta property="og:title" content="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2019-20 - Wikipedia, la enciclopedia libre">
<meta property="og:type" content="website">
<link rel="preconnect" href="//upload.wikimedia.org">
<link rel="alternate" media="only screen and (max-width: 720px)" href="//es.m.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20">
<link rel="alternate" type="application/x-wiki" title="Editar" href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">
<link rel="icon" href="/static/favicon/wikipedia.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (es)">
<link rel="EditURI" type="application/rsd+xml" href="//es.wikipedia.org/w/api.php?action=rsd">
<link rel="canonical" href="https://es.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">
<link rel="alternate" type="application/atom+xml" title="Canal Atom de Wikipedia" href="/w/index.php?title=Especial:CambiosRecientes&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="//login.wikimedia.org">
</head>
<body class="skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-104 ns-subject mw-editable page-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20 rootpage-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20 skin-vector-2022 action-view"><a class="mw-jump-link" href="#bodyContent">Ir al contenido</a>
<div class="vector-header-container">
	<header class="vector-header mw-header">
		<div class="vector-header-start">
			<nav class="vector-main-menu-landmark" aria-label="Sitio" role="navigation">
				
<div id="vector-main-menu-dropdown" class="vector-dropdown vector-main-menu-dropdown vector-button-flush-left vector-button-flush-right"  >
	<input type="checkbox" id="vector-main-menu-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-main-menu-dropdown" class="vector-dropdown-checkbox "  aria-label="Menú principal"  >
	<label id="vector-main-menu-dropdown-label" for="vector-main-menu-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-menu mw-ui-icon-wikimedia-menu"></span>

<span class="vector-dropdown-label-text">Menú principal</span>
	</label>
	<div class="vector-dropdown-content">


				<div id="vector-main-menu-unpinned-container" class="vector-unpinned-container">
		
<div id="vector-main-menu" class="vector-main-menu vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-main-menu-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="main-menu-pinned"
	data-pinnable-element-id="vector-main-menu"
	data-pinned-container-id="vector-main-menu-pinned-container"
	data-unpinned-container-id="vector-main-menu-unpinned-container"
>
	<div class="vector-pinnable-header-label">Menú principal</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-main-menu.pin">mover a la barra lateral</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-main-menu.unpin">ocultar</button>
</div>

	
<div id="p-navigation" class="vector-menu mw-portlet mw-portlet-navigation"  >
	<div class="vector-menu-heading">
		Navegación
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="n-mainpage-description" class="mw-list-item"><a href="/wiki/Wikipedia:Portada" title="Visitar la página principal [z]" accesskey="z"><span>Portada</span></a></li><li id="n-portal" class="mw-list-item"><a href="/wiki/Portal:Comunidad" title="Acerca del proyecto, lo que puedes hacer, dónde encontrar información"><span>Portal de la comunidad</span></a></li><li id="n-currentevents" class="mw-list-item"><a href="/wiki/Portal:Actualidad" title="Encuentra información de contexto sobre acontecimientos actuales"><span>Actualidad</span></a></li><li id="n-recentchanges" class="mw-list-item"><a href="/wiki/Especial:CambiosRecientes" title="Lista de cambios recientes en la wiki [r]" accesskey="r"><span>Cambios recientes</span></a></li><li id="n-newpages" class="mw-list-item"><a href="/wiki/Especial:P%C3%A1ginasNuevas"><span>Páginas nuevas</span></a></li><li id="n-randompage" class="mw-list-item"><a href="/wiki/Especial:Aleatoria" title="Cargar una página al azar [x]" accesskey="x"><span>Página aleatoria</span></a></li><li id="n-help" class="mw-list-item"><a href="/wiki/Ayuda:Contenidos" title="El lugar para aprender"><span>Ayuda</span></a></li><li id="n-sitesupport" class="mw-list-item"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_es.wikipedia.org&amp;uselang=es" title="Apóyanos"><span>Donaciones</span></a></li><li id="n-bug_in_article" class="mw-list-item"><a href="/wiki/Wikipedia:Informes_de_error"><span>Notificar un error</span></a></li>
		</ul>
		
	</div>
</div>

	
	
	
<div class="vector-main-menu-action vector-main-menu-action-lang-alert vector-main-menu-action-lang-alert-empty">
	<div class="vector-main-menu-action-item">
		<div class="vector-main-menu-action-heading vector-menu-heading">Idiomas</div>
		<div class="vector-main-menu-action-content vector-menu-content">
			<div class="mw-message-box cdx-message cdx-message--block mw-message-box-notice cdx-message--notice vector-language-sidebar-alert"><span class="cdx-message__icon"></span><div class="cdx-message__content">Los enlaces de idiomas se encuentran en la parte superior de la página, frente al título.</div></div>
		</div>
	</div>
</div>

</div>

				</div>

	</div>
</div>

		</nav>
			
<a href="/wiki/Wikipedia:Portada" class="mw-logo">
	<img class="mw-logo-icon" src="/static/images/icons/wikipedia.png" alt="" aria-hidden="true" height="50" width="50">
	<span class="mw-logo-container">
		<img class="mw-logo-wordmark" alt="Wikipedia" src="/static/images/mobile/copyright/wikipedia-wordmark-en.svg" style="width: 7.5em; height: 1.125em;">
		<img class="mw-logo-tagline" alt="La enciclopedia libre" src="/static/images/mobile/copyright/wikipedia-tagline-es.svg" width="120" height="13" style="width: 7.5em; height: 0.8125em;">
	</span>
</a>

		</div>
		<div class="vector-header-end">
			
<div id="p-search" role="search" class="vector-search-box-vue  vector-search-box-collapses vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box">
	<a href="/wiki/Especial:Buscar" class="cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only search-toggle" id="" title="Buscar en este wiki [f]" accesskey="f"><span class="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search"></span>

<span>Buscar</span>
	</a>
	<div class="vector-typeahead-search-container">
		<div class="cdx-typeahead-search cdx-typeahead-search--show-thumbnail cdx-typeahead-search--auto-expand-width">
			<form action="/w/index.php" id="searchform" class="cdx-search-input cdx-search-input--has-end-button">
				<div id="simpleSearch" class="cdx-search-input__input-wrapper"  data-search-loc="header-moved">
					<div class="cdx-text-input cdx-text-input--has-start-icon">
						<input
							class="cdx-text-input__input"
							 type="search" name="search" placeholder="Buscar en Wikipedia" aria-label="Buscar en Wikipedia" autocapitalize="sentences" title="Buscar en este wiki [f]" accesskey="f" id="searchInput"
							>
						<span class="cdx-text-input__icon cdx-text-input__start-icon"></span>
					</div>
					<input type="hidden" name="title" value="Especial:Buscar">
				</div>
				<button class="cdx-button cdx-search-input__end-button">Buscar</button>
			</form>
		</div>
	</div>
</div>

			<nav class="vector-user-links vector-user-links-wide" aria-label="Herramientas personales" role="navigation" >
	<div class="vector-user-links-main">
	
<div id="p-vector-user-menu-preferences" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	
<div id="p-vector-user-menu-userpage" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	<nav class="vector-client-prefs-landmark" aria-label="Tema">
		
		
	</nav>
	
<div id="p-vector-user-menu-notifications" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	
<div id="p-vector-user-menu-overflow" class="vector-menu mw-portlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			<li id="pt-createaccount-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio" class=""><span>Crear una cuenta</span></a>
</li>
<li id="pt-login-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o" class=""><span>Acceder</span></a>
</li>

			
		</ul>
		
	</div>
</div>

	</div>
	
<div id="vector-user-links-dropdown" class="vector-dropdown vector-user-menu vector-button-flush-right vector-user-menu-logged-out"  title="Más opciones" >
	<input type="checkbox" id="vector-user-links-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-user-links-dropdown" class="vector-dropdown-checkbox "  aria-label="Herramientas personales"  >
	<label id="vector-user-links-dropdown-label" for="vector-user-links-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-ellipsis mw-ui-icon-wikimedia-ellipsis"></span>

<span class="vector-dropdown-label-text">Herramientas personales</span>
	</label>
	<div class="vector-dropdown-content">


		
<div id="p-personal" class="vector-menu mw-portlet mw-portlet-personal user-links-collapsible-item"  title="Menú de usuario" >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="pt-createaccount" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio"><span class="vector-icon mw-ui-icon-userAdd mw-ui-icon-wikimedia-userAdd"></span> <span>Crear una cuenta</span></a></li><li id="pt-login" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o"><span class="vector-icon mw-ui-icon-logIn mw-ui-icon-wikimedia-logIn"></span> <span>Acceder</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-user-menu-anon-editor" class="vector-menu mw-portlet mw-portlet-user-menu-anon-editor"  >
	<div class="vector-menu-heading">
		Páginas para editores desconectados <a href="/wiki/Ayuda:Introducci%C3%B3n" aria-label="Obtenga más información sobre editar"><span>más información</span></a>
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="pt-anoncontribs" class="mw-list-item"><a href="/wiki/Especial:MisContribuciones" title="Una lista de modificaciones hechas desde esta dirección IP [y]" accesskey="y"><span>Contribuciones</span></a></li><li id="pt-anontalk" class="mw-list-item"><a href="/wiki/Especial:MiDiscusi%C3%B3n" title="Discusión sobre ediciones hechas desde esta dirección IP [n]" accesskey="n"><span>Discusión</span></a></li>
		</ul>
		
	</div>
</div>

	
	</div>
</div>

</nav>

		</div>
	</header>
</div>
<div class="mw-page-container">
	<div class="mw-page-container-inner">
		<div class="vector-sitenotice-container">
			<div id="siteNotice"><!-- CentralNotice --></div>
		</div>
		<div class="vector-column-start">
			<div class="vector-main-menu-container">
		<div id="mw-navigation">
			<nav id="mw-panel" class="vector-main-menu-landmark" aria-label="Sitio" role="navigation">
				<div id="vector-main-menu-pinned-container" class="vector-pinned-container">
				
				</div>
		</nav>
		</div>
	</div>
	<div class="vector-sticky-pinned-container">
				<nav id="mw-panel-toc" role="navigation" aria-label="Contenidos" data-event-name="ui.sidebar-toc" class="mw-table-of-contents-container vector-toc-landmark">
					<div id="vector-toc-pinned-container" class="vector-pinned-container">
					<div id="vector-toc" class="vector-toc vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-toc-pinnable-header vector-pinnable-header-pinned"
	data-feature-name="toc-pinned"
	data-pinnable-element-id="vector-toc"
	
	
>
	<h2 class="vector-pinnable-header-label">Contenidos</h2>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-toc.pin">mover a la barra lateral</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-toc.unpin">ocultar</button>
</div>


	<ul class="vector-toc-contents" id="mw-panel-toc-list">
		<li id="toc-mw-content-text"
			class="vector-toc-list-item vector-toc-level-1">
			<a href="#" class="vector-toc-link">
				<div class="vector-toc-text">Inicio</div>
			</a>
		</li>
		<li id="toc-Cuadro_de_clasificación"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Cuadro_de_clasificación">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">1</span>Cuadro de clasificación</div>
		</a>
		
		<ul id="toc-Cuadro_de_clasificación-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Participantes"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Participantes">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">2</span>Participantes</div>
		</a>
		
		<ul id="toc-Participantes-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Estadios"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Estadios">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">3</span>Estadios</div>
		</a>
		
		<ul id="toc-Estadios-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Llaves"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Llaves">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">4</span>Llaves</div>
		</a>
		
		<ul id="toc-Llaves-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Enfrentamientos"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Enfrentamientos">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">5</span>Enfrentamientos</div>
		</a>
		
			<button aria-controls="toc-Enfrentamientos-sublist" class="cdx-button cdx-button--weight-quiet cdx-button--icon-only vector-toc-toggle">
				<span class="vector-icon vector-icon--x-small mw-ui-icon-wikimedia-expand"></span>
				<span>Alternar subsección Enfrentamientos</span>
			</button>
		
		<ul id="toc-Enfrentamientos-sublist" class="vector-toc-list">
			<li id="toc-Borussia_Dortmund_–_París_Saint-Germain"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Borussia_Dortmund_–_París_Saint-Germain">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.1</span>Borussia Dortmund – París Saint-Germain</div>
			</a>
			
			<ul id="toc-Borussia_Dortmund_–_París_Saint-Germain-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Real_Madrid_–_Manchester_City"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Real_Madrid_–_Manchester_City">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.2</span>Real Madrid – Manchester City</div>
			</a>
			
			<ul id="toc-Real_Madrid_–_Manchester_City-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Atalanta_–_Valencia"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Atalanta_–_Valencia">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.3</span>Atalanta – Valencia</div>
			</a>
			
			<ul id="toc-Atalanta_–_Valencia-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Atlético_de_Madrid_–_Liverpool"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Atlético_de_Madrid_–_Liverpool">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.4</span>Atlético de Madrid – Liverpool</div>
			</a>
			
			<ul id="toc-Atlético_de_Madrid_–_Liverpool-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Chelsea_–_Bayern_de_Múnich"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Chelsea_–_Bayern_de_Múnich">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.5</span>Chelsea – Bayern de Múnich</div>
			</a>
			
			<ul id="toc-Chelsea_–_Bayern_de_Múnich-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Olympique_de_Lyon_–_Juventus"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Olympique_de_Lyon_–_Juventus">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.6</span>Olympique de Lyon – Juventus</div>
			</a>
			
			<ul id="toc-Olympique_de_Lyon_–_Juventus-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Tottenham_Hotspur_–_Leipzig"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Tottenham_Hotspur_–_Leipzig">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.7</span>Tottenham Hotspur – Leipzig</div>
			</a>
			
			<ul id="toc-Tottenham_Hotspur_–_Leipzig-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Napoli_–_Barcelona"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Napoli_–_Barcelona">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.8</span>Napoli – Barcelona</div>
			</a>
			
			<ul id="toc-Napoli_–_Barcelona-sublist" class="vector-toc-list">
			</ul>
		</li>
	</ul>
	</li>
	<li id="toc-Clasificados_para_cuartos_de_final"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Clasificados_para_cuartos_de_final">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">6</span>Clasificados para cuartos de final</div>
		</a>
		
		<ul id="toc-Clasificados_para_cuartos_de_final-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Véase_también"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Véase_también">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">7</span>Véase también</div>
		</a>
		
		<ul id="toc-Véase_también-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Enlaces_externos"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Enlaces_externos">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">8</span>Enlaces externos</div>
		</a>
		
		<ul id="toc-Enlaces_externos-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Referencias"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Referencias">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">9</span>Referencias</div>
		</a>
		
		<ul id="toc-Referencias-sublist" class="vector-toc-list">
		</ul>
	</li>
</ul>
</div>

					</div>
		</nav>
			</div>
		</div>
		<div class="mw-content-container">
			<main id="content" class="mw-body" role="main">
				<header class="mw-body-header vector-page-titlebar">
					<nav role="navigation" aria-label="Contenidos" class="vector-toc-landmark">
						
<div id="vector-page-titlebar-toc" class="vector-dropdown vector-page-titlebar-toc vector-button-flush-left"  >
	<input type="checkbox" id="vector-page-titlebar-toc-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-page-titlebar-toc" class="vector-dropdown-checkbox "  aria-label="Cambiar a la tabla de contenidos"  >
	<label id="vector-page-titlebar-toc-label" for="vector-page-titlebar-toc-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-listBullet mw-ui-icon-wikimedia-listBullet"></span>

<span class="vector-dropdown-label-text">Cambiar a la tabla de contenidos</span>
	</label>
	<div class="vector-dropdown-content">


							<div id="vector-page-titlebar-toc-unpinned-container" class="vector-unpinned-container">
			</div>
		
	</div>
</div>

					</nav>
					<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-namespace">Anexo</span><span class="mw-page-title-separator">:</span><span class="mw-page-title-main">Octavos de final de la Liga de Campeones de la UEFA 2019-20</span></h1>
							
<div id="p-lang-btn" class="vector-dropdown mw-portlet mw-portlet-lang"  >
	<input type="checkbox" id="p-lang-btn-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-lang-btn" class="vector-dropdown-checkbox mw-interlanguage-selector" aria-label="Este artículo existe sólo en este idioma. Añade el artículo para otros idiomas"   >
	<label id="p-lang-btn-label" for="p-lang-btn-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--action-progressive mw-portlet-lang-heading-0" aria-hidden="true"  ><span class="vector-icon mw-ui-icon-language-progressive mw-ui-icon-wikimedia-language-progressive"></span>

<span class="vector-dropdown-label-text">Añadir idiomas</span>
	</label>
	<div class="vector-dropdown-content">

		<div class="vector-menu-content">
			
			<ul class="vector-menu-content-list">
				
				
			</ul>
			<div class="after-portlet after-portlet-lang"><span class="uls-after-portlet-link"></span><span class="wb-langlinks-add wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:NewItem?site=eswiki&amp;page=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20" title="Agregar enlaces interlingüísticos" class="wbc-editpage">Añadir enlaces</a></span></div>
		</div>

	</div>
</div>
</header>
				<div class="vector-page-toolbar">
					<div class="vector-page-toolbar-container">
						<div id="left-navigation">
							<nav aria-label="Espacios de nombres">
								
<div id="p-associated-pages" class="vector-menu vector-menu-tabs mw-portlet mw-portlet-associated-pages"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-nstab-anexo" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Ver la página de contenido [c]" accesskey="c"><span>Anexo</span></a></li><li id="ca-talk" class="new vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo_discusi%C3%B3n:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;redlink=1" rel="discussion" title="Discusión acerca de la página (aún no redactado) [t]" accesskey="t"><span>Discusión</span></a></li>
		</ul>
		
	</div>
</div>

								
<div id="p-variants" class="vector-dropdown emptyPortlet"  >
	<input type="checkbox" id="p-variants-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-variants" class="vector-dropdown-checkbox " aria-label="Cambiar variante de idioma"   >
	<label id="p-variants-label" for="p-variants-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" aria-hidden="true"  ><span class="vector-dropdown-label-text">español</span>
	</label>
	<div class="vector-dropdown-content">


					
<div id="p-variants" class="vector-menu mw-portlet mw-portlet-variants emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

				
	</div>
</div>

							</nav>
						</div>
						<div id="right-navigation" class="vector-collapsible">
							<nav aria-label="Vistas">
								
<div id="p-views" class="vector-menu vector-menu-tabs mw-portlet mw-portlet-views"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-view" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20"><span>Leer</span></a></li><li id="ca-edit" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-history" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=history" title="Versiones anteriores de esta página [h]" accesskey="h"><span>Ver historial</span></a></li>
		</ul>
		
	</div>
</div>

							</nav>
				
							<nav class="vector-page-tools-landmark" aria-label="Página de herramientas">
								
<div id="vector-page-tools-dropdown" class="vector-dropdown vector-page-tools-dropdown"  >
	<input type="checkbox" id="vector-page-tools-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-page-tools-dropdown" class="vector-dropdown-checkbox "  aria-label="Herramientas"  >
	<label id="vector-page-tools-dropdown-label" for="vector-page-tools-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" aria-hidden="true"  ><span class="vector-dropdown-label-text">Herramientas</span>
	</label>
	<div class="vector-dropdown-content">


									<div id="vector-page-tools-unpinned-container" class="vector-unpinned-container">
						
<div id="vector-page-tools" class="vector-page-tools vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-page-tools-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="page-tools-pinned"
	data-pinnable-element-id="vector-page-tools"
	data-pinned-container-id="vector-page-tools-pinned-container"
	data-unpinned-container-id="vector-page-tools-unpinned-container"
>
	<div class="vector-pinnable-header-label">Herramientas</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-page-tools.pin">mover a la barra lateral</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-page-tools.unpin">ocultar</button>
</div>

	
<div id="p-cactions" class="vector-menu mw-portlet mw-portlet-cactions emptyPortlet vector-has-collapsible-items"  title="Más opciones" >
	<div class="vector-menu-heading">
		Acciones
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-more-view" class="selected vector-more-collapsible-item mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20"><span>Leer</span></a></li><li id="ca-more-edit" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-more-history" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=history"><span>Ver historial</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-tb" class="vector-menu mw-portlet mw-portlet-tb"  >
	<div class="vector-menu-heading">
		General
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-whatlinkshere" class="mw-list-item"><a href="/wiki/Especial:LoQueEnlazaAqu%C3%AD/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Lista de todas las páginas de la wiki que enlazan aquí [j]" accesskey="j"><span>Lo que enlaza aquí</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/wiki/Especial:CambiosEnEnlazadas/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" rel="nofollow" title="Cambios recientes en las páginas que enlazan con esta [k]" accesskey="k"><span>Cambios en enlazadas</span></a></li><li id="t-upload" class="mw-list-item"><a href="//commons.wikimedia.org/wiki/Special:UploadWizard?uselang=es" title="Subir archivos [u]" accesskey="u"><span>Subir archivo</span></a></li><li id="t-specialpages" class="mw-list-item"><a href="/wiki/Especial:P%C3%A1ginasEspeciales" title="Lista de todas las páginas especiales [q]" accesskey="q"><span>Páginas especiales</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;oldid=154476111" title="Enlace permanente a esta versión de la página"><span>Enlace permanente</span></a></li><li id="t-info" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=info" title="Más información sobre esta página"><span>Información de la página</span></a></li><li id="t-cite" class="mw-list-item"><a href="/w/index.php?title=Especial:Citar&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;id=154476111&amp;wpFormIdentifier=titleform" title="Información sobre cómo citar esta página"><span>Citar esta página</span></a></li><li id="t-urlshortener" class="mw-list-item"><a href="/w/index.php?title=Especial:Acortador_de_URL&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20"><span>Obtener URL acortado</span></a></li><li id="t-urlshortener-qrcode" class="mw-list-item"><a href="/w/index.php?title=Especial:QrCode&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20"><span>Download QR code</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-coll-print_export" class="vector-menu mw-portlet mw-portlet-coll-print_export"  >
	<div class="vector-menu-heading">
		Imprimir/exportar
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="coll-create_a_book" class="mw-list-item"><a href="/w/index.php?title=Especial:Libro&amp;bookcmd=book_creator&amp;referer=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20"><span>Crear un libro</span></a></li><li id="coll-download-as-rl" class="mw-list-item"><a href="/w/index.php?title=Especial:DownloadAsPdf&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=show-download-screen"><span>Descargar como PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;printable=yes" title="Versión imprimible de esta página [p]" accesskey="p"><span>Versión para imprimir</span></a></li>
		</ul>
		
	</div>
</div>

</div>

									</div>
				
	</div>
</div>

							</nav>
						</div>
					</div>
				</div>
				<div class="vector-column-end">
					<div class="vector-sticky-pinned-container">
						<nav class="vector-page-tools-landmark" aria-label="Página de herramientas">
							<div id="vector-page-tools-pinned-container" class="vector-pinned-container">
				
							</div>
		</nav>
						<nav class="vector-client-prefs-landmark" aria-label="Tema">
						</nav>
					</div>
				</div>
				<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>
					<div class="vector-body-before-content">
							<div class="mw-indicators">
		</div>

						<div id="siteSub" class="noprint">De Wikipedia, la enciclopedia libre</div>
					</div>
					<div id="contentSub"><div id="mw-content-subtitle"></div></div>
					
					
					<div id="mw-content-text" class="mw-body-content"><div class="mw-content-ltr mw-parser-output" lang="es" dir="ltr"><div class="noprint AP rellink"><span style="font-size:88%">Artículo principal:</span>&#32;<i><a href="/wiki/Liga_de_Campeones_de_la_UEFA_2019-20" title="Liga de Campeones de la UEFA 2019-20"> Liga de Campeones de la UEFA 2019-20</a></i></div>
<p>En los <b>Octavos de final de la <a href="/wiki/Liga_de_Campeones_de_la_UEFA_2019-20" title="Liga de Campeones de la UEFA 2019-20">Liga de Campeones de la UEFA 2019-20</a></b>, participaron los dieciséis equipos que terminaron primeros y segundos de cada grupo en la fase anterior. Estos fueron distribuidos en ocho parejas. Cada pareja se enfrentó en partidos de ida y vuelta de 90 minutos cada uno. En estos encuentros rigió la <a href="/wiki/Regla_del_gol_de_visitante" title="Regla del gol de visitante">regla del gol de visitante</a>, que determina que el equipo que haya convertido más goles como visitante gana si hay empate en la diferencia de goles. En caso de que no hubiese ganador en el período regular, se realizó una prórroga de 30 minutos, y si no hubo ganador se realizaron <a href="/wiki/Tiros_desde_el_punto_penal" title="Tiros desde el punto penal">tiros desde el punto penal</a>.
</p>
<meta property="mw:PageProp/toc" />
<h2><span id="Cuadro_de_clasificaci.C3.B3n"></span><span class="mw-headline" id="Cuadro_de_clasificación">Cuadro de clasificación</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=1" title="Editar sección: Cuadro de clasificación"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="columns" style="-moz-column-count:2; -webkit-column-count:2; column-count:2;">
</div>
<center>
<table cellspacing="0" style="background: #f9f9f9; border: 1px #aaa solid; border-collapse: collapse;" width="60%">

<tbody><tr style="color:black" bgcolor="#ccddcc">
<th>Grupo
</th>
<th>Bombo 1<br /><span style="white-space:nowrap">(Líderes de grupo)</span>
</th>
<th>Bombo 2<br /><span style="white-space:nowrap">(Segundos de grupo)</span>
</th></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2019-20">A</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2019-20">B</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern de Múnich</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2019-20">C</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City" class="mw-redirect" title="Manchester City">Manchester City</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Atalanta_B.C." class="mw-redirect" title="Atalanta B.C.">Atalanta</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2019-20">D</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2019-20">E</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Societa_Sportiva_Calcio_Napoli" class="mw-redirect" title="Societa Sportiva Calcio Napoli">Napoli</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2019-20">F</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2019-20">G</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2019-20">H</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Valencia_Club_de_F%C3%BAtbol" title="Valencia Club de Fútbol">Valencia</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</td></tr></tbody></table>
</center>
<h2><span class="mw-headline" id="Participantes">Participantes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=2" title="Editar sección: Participantes"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table width="100%">

<tbody><tr align="center">
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</th>
<th><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</th>
<th><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</th>
<th><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</th>
<th><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</th>
<th><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a>
</th>
<th><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</th>
<th><a href="/wiki/Valencia_Club_de_F%C3%BAtbol" title="Valencia Club de Fútbol">Valencia</a>
</th></tr>
<tr>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4f/Kit_left_arm_psg1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b3/Kit_body_psg1920H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f1/Kit_right_arm_psg1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000040"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/12/Kit_left_arm_bayern1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/38/Kit_body_bayern1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_bayern1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1b/Kit_shorts_bayern1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#D50000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_red.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_socks_3_stripes_red.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#84BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/58/Kit_left_arm_mancity1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#84BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a9/Kit_body_mancity1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#84BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1b/Kit_right_arm_mancity1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_mancity1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_shorts_mancity1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/0e/Kit_socks_mancity1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/33/Kit_body_juventus1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ger18h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a2/Kit_shorts_ger18h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4e/Kit_socks_juventus1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/07/Kit_left_arm_liverpool1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fc/Kit_body_liverpool1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fa/Kit_right_arm_liverpool1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/cf/Kit_socks_liverpool1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcbarcelona1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_left_arm_fcbarcelona1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcbarcelona1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/da/Kit_body_fcbarcelona1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcbarcelona1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9a/Kit_right_arm_fcbarcelona1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000080"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_barcelona1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_socks_barcelona1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_rbl1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/27/Kit_left_arm_rbl1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rblei1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_rblei1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_rbl1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9d/Kit_right_arm_rbl1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/ce/Kit_left_arm_valenciacf1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d6/Kit_body_valenciacf1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_right_arm_valenciacf1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/68/Kit_shorts_valenciacf1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_valenciacf1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/d7/Kit_socks_valenciacf1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th></tr>
<tr align="center">
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th></tr></tbody></table>
<table width="100%">

<tbody><tr align="center">
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</th>
<th><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</th>
<th><a href="/wiki/Atalanta_Bergamasca_Calcio" title="Atalanta Bergamasca Calcio">Atalanta</a>
</th>
<th><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</th>
<th><a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a>
</th>
<th><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</th>
<th><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</th>
<th><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</th></tr>
<tr>
<th>Eliminado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cb/Kit_left_arm_realmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d9/Kit_body_realmadrid1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_right_arm_realmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0d/Kit_shorts_realmadrid1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/a1/Kit_socks_realmadrid1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a1/Kit_left_arm_tottenham1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d3/Kit_body_tottenham1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/42/Kit_right_arm_tottenham1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/1/12/Kit_socks_tottenham1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_left_arm_atalanta1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_body_atalanta1920H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_right_arm_atalanta1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c0/Kit_shorts_atalanta1920H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atalanta1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/05/Kit_socks_atalanta1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_left_arm_atlmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7e/Kit_body_atlmadrid1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/03/Kit_right_arm_atlmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atlmadrid1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b1/Kit_socks_atlmadrid1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/10/Kit_left_arm_napoli1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/29/Kit_body_napoli1920e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_right_arm_napoli1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/40/Kit_shorts_napoli1920e.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#ffffff"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_napoli1920H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/2/29/Kit_socks_napoli1920H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6c/Kit_left_arm_bvb1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/91/Kit_body_bvb1920e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c2/Kit_right_arm_bvb1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bvb1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/92/Kit_shorts_bvb1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb1920e.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fb/Kit_socks_bvb1920e.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e0/Kit_left_arm_ol1920c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5d/Kit_body_ol1920c.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_right_arm_ol1920c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_shorts_ol1920c.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_lafc19A.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_socks_lafc19A.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5b/Kit_left_arm_chelsea1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_body_chelsea1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cb/Kit_right_arm_chelsea1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/ca/Kit_socks_chelsea1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th></tr>
<tr align="center">
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th></tr></tbody></table>
<h2><span class="mw-headline" id="Estadios">Estadios</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=3" title="Editar sección: Estadios"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:ParcDesPrincesII.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ParcDesPrincesII.jpg/200px-ParcDesPrincesII.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ParcDesPrincesII.jpg/300px-ParcDesPrincesII.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ParcDesPrincesII.jpg/400px-ParcDesPrincesII.jpg 2x" data-file-width="1024" data-file-height="767" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:M%C3%BCnchen_-_Allianz-Arena_(Luftbild).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/200px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/300px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/400px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg 2x" data-file-width="1484" data-file-height="840" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Etihad_Stadium_at_night_-_2015.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/200px-Etihad_Stadium_at_night_-_2015.jpg" decoding="async" width="200" height="105" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/300px-Etihad_Stadium_at_night_-_2015.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/400px-Etihad_Stadium_at_night_-_2015.jpg 2x" data-file-width="1024" data-file-height="537" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Juventus_v_Real_Madrid,_Champions_League,_Stadium,_Turin,_2013.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg/200px-Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg/300px-Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg/400px-Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg 2x" data-file-width="4608" data-file-height="2592" /></a></span>
</td></tr>
<tr align="center">
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a></b><br />
<p>Ciudad: <a href="/wiki/Par%C3%ADs" title="París">París</a><br />
Capacidad: <b>47.500</b> espectadores<br />
Club: <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</p>
</td>
<td><b><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a></b><br />
<p>Ciudad: <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a><br />
Capacidad: <b>75.024</b> espectadores<br />
Club: <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern de Múnich</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a></b><br />
<p>Ciudad: <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a><br />
Capacidad: <b>55.097</b> espectadores<br />
Club: <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</p>
</td>
<td><b><a href="/wiki/Juventus_Stadium" title="Juventus Stadium">Allianz Stadium</a></b><br />
<p>Ciudad: <a href="/wiki/Tur%C3%ADn" title="Turín">Turín</a><br />
Capacidad: <b>41.000</b> espectadores<br />
Club: <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Panorama_of_Anfield_with_new_main_stand_(29676137824).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/200px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg" decoding="async" width="200" height="136" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/300px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/400px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 2x" data-file-width="3148" data-file-height="2143" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Camp_Nou_aerial_(cropped).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Camp_Nou_aerial_%28cropped%29.jpg/200px-Camp_Nou_aerial_%28cropped%29.jpg" decoding="async" width="200" height="130" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Camp_Nou_aerial_%28cropped%29.jpg/300px-Camp_Nou_aerial_%28cropped%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Camp_Nou_aerial_%28cropped%29.jpg/400px-Camp_Nou_aerial_%28cropped%29.jpg 2x" data-file-width="1826" data-file-height="1186" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Red_Bull_arena,_Leipzig_von_oben_Zentralstadion.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Red_Bull_arena%2C_Leipzig_von_oben_Zentralstadion.jpg/200px-Red_Bull_arena%2C_Leipzig_von_oben_Zentralstadion.jpg" decoding="async" width="200" height="131" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Red_Bull_arena%2C_Leipzig_von_oben_Zentralstadion.jpg/300px-Red_Bull_arena%2C_Leipzig_von_oben_Zentralstadion.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Red_Bull_arena%2C_Leipzig_von_oben_Zentralstadion.jpg/400px-Red_Bull_arena%2C_Leipzig_von_oben_Zentralstadion.jpg 2x" data-file-width="2525" data-file-height="1649" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG/200px-CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG/300px-CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG/400px-CAMP_DE_MESTALLA_GRADA_DE_LA_MAR_2014.JPG 2x" data-file-width="5184" data-file-height="3456" /></a></span>
</td></tr>
<tr align="center">
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Anfield" title="Anfield">Anfield</a></b><br />
<p>Ciudad: <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a><br />
Capacidad: <b>54.074</b> espectadores<br />
Club: <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</p>
</td>
<td><b><a href="/wiki/Camp_Nou" title="Camp Nou">Camp Nou</a></b><br />
<p>Ciudad: <a href="/wiki/Barcelona" title="Barcelona">Barcelona</a><br />
Capacidad: <b>99.354</b> espectadores<br />
Club: <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a>
</p>
</td>
<td><b><a href="/wiki/Red_Bull_Arena_(Leipzig)" title="Red Bull Arena (Leipzig)">Red Bull Arena</a></b><br />
<p>Ciudad: <a href="/wiki/Leipzig" title="Leipzig">Leipzig</a><br />
Capacidad: <b>44.199</b> espectadores<br />
Club: <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_de_Mestalla" title="Estadio de Mestalla">Mestalla</a></b><br />
<p>Ciudad: <a href="/wiki/Valencia" title="Valencia">Valencia</a><br />
Capacidad: <b>48.600</b> espectadores<br />
Club: <a href="/wiki/Valencia_CF" class="mw-redirect" title="Valencia CF">Valencia</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c8/The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg/200px-The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c8/The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg/300px-The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c8/The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg/400px-The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg 2x" data-file-width="3264" data-file-height="2448" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg/200px-Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg/300px-Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg/400px-Tottenham_Hotspur_Stadium_March_2019_-_view_from_east.jpg 2x" data-file-width="4601" data-file-height="3068" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Stadio_San_Siro.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Stadio_San_Siro.jpg/200px-Stadio_San_Siro.jpg" decoding="async" width="200" height="86" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Stadio_San_Siro.jpg/300px-Stadio_San_Siro.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Stadio_San_Siro.jpg/400px-Stadio_San_Siro.jpg 2x" data-file-width="640" data-file-height="275" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Estadio_Wanda_Metropolitano_(2018).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/200px-Estadio_Wanda_Metropolitano_%282018%29.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/300px-Estadio_Wanda_Metropolitano_%282018%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/400px-Estadio_Wanda_Metropolitano_%282018%29.jpg 2x" data-file-width="4896" data-file-height="3672" /></a></span>
</td></tr>
<tr align="center">
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a></b><br />
<p>Ciudad: <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>81.044</b> espectadores<br />
Club: <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</p>
</td>
<td><a href="/wiki/Tottenham_Hotspur_Stadium" title="Tottenham Hotspur Stadium">Tottenham Hotspur Stadium</a><br />
<p>Ciudad: <a href="/wiki/Londres" title="Londres">Londres</a><br />
Capacidad: <b>62.062</b> espectadores<br />
Club: <a href="/wiki/Tottenham_Hotspur" class="mw-redirect" title="Tottenham Hotspur">Tottenham Hotspur</a>
</p>
</td>
<td><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">San Siro</a> <br />
<p>Ciudad: <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a><br />
Capacidad: <b>80.018</b> espectadores<br />
Club: <a href="/wiki/Atalanta_B.C." class="mw-redirect" title="Atalanta B.C.">Atalanta</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Metropolitano_(Madrid)" title="Estadio Metropolitano (Madrid)">Wanda Metropolitano</a></b><br />
<p>Ciudad: <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>67.703</b> espectadores<br />
Club: <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:San_Paolo_-_Curva_A.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6c/San_Paolo_-_Curva_A.jpg/200px-San_Paolo_-_Curva_A.jpg" decoding="async" width="200" height="135" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6c/San_Paolo_-_Curva_A.jpg/300px-San_Paolo_-_Curva_A.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6c/San_Paolo_-_Curva_A.jpg/400px-San_Paolo_-_Curva_A.jpg 2x" data-file-width="2015" data-file-height="1356" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Signal_Iduna_Park_new_sign.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Signal_Iduna_Park_new_sign.jpg/200px-Signal_Iduna_Park_new_sign.jpg" decoding="async" width="200" height="97" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Signal_Iduna_Park_new_sign.jpg/300px-Signal_Iduna_Park_new_sign.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Signal_Iduna_Park_new_sign.jpg/400px-Signal_Iduna_Park_new_sign.jpg 2x" data-file-width="3776" data-file-height="1840" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Parc_OL.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/Parc_OL.jpg/200px-Parc_OL.jpg" decoding="async" width="200" height="112" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/Parc_OL.jpg/300px-Parc_OL.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/13/Parc_OL.jpg/400px-Parc_OL.jpg 2x" data-file-width="2592" data-file-height="1456" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Stamford_Bridge.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Stamford_Bridge.jpg/200px-Stamford_Bridge.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Stamford_Bridge.jpg/300px-Stamford_Bridge.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Stamford_Bridge.jpg/400px-Stamford_Bridge.jpg 2x" data-file-width="1024" data-file-height="768" /></a></span>
</td></tr>
<tr align="center">
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Estadio_San_Paolo" class="mw-redirect" title="Estadio San Paolo">Estadio San Paolo</a></b><br />
<p>Ciudad: <a href="/wiki/N%C3%A1poles" title="Nápoles">Nápoles</a><br />
Capacidad: <i>55.000</i> espectadores<br />
Club: <a href="/wiki/SSC_Napoli" class="mw-redirect" title="SSC Napoli">Napoli</a>
</p>
</td>
<td><b><a href="/wiki/Signal_Iduna_Park" title="Signal Iduna Park">Signal Iduna Park</a></b><br />
<p>Ciudad: <a href="/wiki/Dortmund" title="Dortmund">Dortmund</a><br />
Capacidad: 81.360 espectadores<br />
Club: <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</p>
</td>
<td><b><a href="/wiki/Parc_Olympique_Lyonnais" title="Parc Olympique Lyonnais">Parc Olympique Lyonnais</a></b><br />
<p>Ciudad: <a href="/wiki/Lyon" title="Lyon">Lyon</a><br />
Capacidad: <b>59.186</b> espectadores<br />
Club: <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</p>
</td>
<td><b><a href="/wiki/Stamford_Bridge_(estadio)" title="Stamford Bridge (estadio)">Stamford Bridge</a></b><br />
<p>Ciudad: <a href="/wiki/Londres" title="Londres">Londres</a><br />
Capacidad: <b>41.837</b> espectadores<br />
Club: <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</p>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Llaves">Llaves</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=4" title="Editar sección: Llaves"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table class="wikitable" style="text-align:center">



<tbody><tr>
<th style="text-align:right; width:250px">Equipo 1
</th>
<th style="width:80px"><abbr title="Resultado global">Agr.</abbr>
</th>
<th style="text-align:left; width:250px">Equipo 2
</th>
<th style="width:80px">Ida
</th>
<th style="width:80px">Vuelta
</th></tr>
<tr>
<td style="text-align: right;"><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">2–3
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <b><a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BOR_PSG">2–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#PSG_BOR">0–2</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="text-align: center;">2–4
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#RMA_MAN">1–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MAN_RMA">1–2</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Atalanta_Bergamasca_Calcio" title="Atalanta Bergamasca Calcio">Atalanta</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="text-align: center;">8–4
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Valencia_Club_de_F%C3%BAtbol" title="Valencia Club de Fútbol">Valencia</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#ATA_VAL">4–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#VAL_ATA">4–3</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="text-align: center;">4–2 <small>(<a href="/wiki/Pr%C3%B3rroga_(deporte)" title="Prórroga (deporte)">t. s.</a>)</small>
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#ATM_LIV">1–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LIV_ATM">3–2</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;">1–7
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <b><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#CHE_BAY">0–3</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BAY_CHE">1–4</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">2–2 <small>(<a href="/wiki/Regla_del_gol_de_visitante" title="Regla del gol de visitante">v.</a>)</small>
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LYO_JUV">1–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#JUV_LYO">1–2</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;">0–4
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <b><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#TOT_RBL">0–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#RBL_TOT">0–3</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="text-align: center;">2–4
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <b><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#NAP_BAR">1–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BAR_NAP">1–3</a>
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Enfrentamientos">Enfrentamientos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=5" title="Editar sección: Enfrentamientos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<h4><span id="Borussia_Dortmund_.E2.80.93_Par.C3.ADs_Saint-Germain"></span><span class="mw-headline" id="Borussia_Dortmund_–_París_Saint-Germain">Borussia Dortmund – París Saint-Germain</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=6" title="Editar sección: Borussia Dortmund – París Saint-Germain"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BOR_PSG">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 18 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:1</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Signal_Iduna_Park" title="Signal Iduna Park">Signal Iduna Park</a>,</span> <a href="/wiki/Dortmund" title="Dortmund">Dortmund</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Erling_Braut_H%C3%A5land" class="mw-redirect" title="Erling Braut Håland">Håland</a> <span typeof="mw:File"><span title="Anotado en el minuto 69"><img alt="Anotado en el minuto 69" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">69'</small> <span typeof="mw:File"><span title="Anotado en el minuto 77"><img alt="Anotado en el minuto 77" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">77'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027120/index.html">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 75"><img alt="Anotado en el minuto 75" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">75'</small> <a href="/wiki/Neymar" title="Neymar">Neymar</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 66&#160;099 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Antonio_Miguel_Mateu_Lahoz" class="mw-redirect" title="Antonio Miguel Mateu Lahoz">Antonio Miguel Mateu Lahoz</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Alejandro José Hernández Hernández</a><br />Jugador del partido: <a href="/wiki/Erling_Braut_H%C3%A5land" class="mw-redirect" title="Erling Braut Håland">Erling Braut Håland</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6c/Kit_left_arm_bvb1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/91/Kit_body_bvb1920e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c2/Kit_right_arm_bvb1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bvb1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/92/Kit_shorts_bvb1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb1920e.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fb/Kit_socks_bvb1920e.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e7/Kit_body_psg1920t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_psg1920t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/1/1c/Kit_socks_psg1920t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="PSG_BOR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 11 de marzo de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:0 <style data-mw-deduplicate="TemplateStyles:r144106874">.mw-parser-output .sinnegrita,.mw-parser-output .sinnegrita b{font-weight:normal}</style><span class="sinnegrita">(2:0)</span></b> </div><div style="font-size: 85%">(Global <b>3:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parc des Princes</a>,</span> <a href="/wiki/Par%C3%ADs" title="París">París</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Neymar" title="Neymar">Neymar</a> <span typeof="mw:File"><span title="Anotado en el minuto 28"><img alt="Anotado en el minuto 28" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">28'</small></li>
<li><a href="/wiki/Juan_Bernat" title="Juan Bernat">Bernat</a> <span typeof="mw:File"><span title="Anotado en el minuto 45+1"><img alt="Anotado en el minuto 45+1" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">45+1'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027130/index.html">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 0 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Anthony_Taylor_(%C3%A1rbitro)" title="Anthony Taylor (árbitro)">Anthony Taylor</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/w/index.php?title=Stuart_Attwell&amp;action=edit&amp;redlink=1" class="new" title="Stuart Attwell (aún no redactado)">Stuart Attwell</a><br />Jugador del partido: <a href="/wiki/Juan_Bernat" title="Juan Bernat">Juan Bernat</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

<tr>
<td align="left" colspan="7" style="font-size:85%;text-align:left">Partido disputado a puerta cerrada (sin público) debido al brote del <a href="/wiki/SARS-CoV-2" title="SARS-CoV-2">Coronavirus-2 del Síndrome Respiratorio Agudo Grave</a> que afecta a numerosas partes del mundo.<sup id="cite_ref-1" class="reference separada"><a href="#cite_note-1"><span class="corchete-llamada">[</span>1<span class="corchete-llamada">]</span></a></sup>&#8203;
</td></tr></tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4f/Kit_left_arm_psg1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b3/Kit_body_psg1920H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f1/Kit_right_arm_psg1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000040"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fb/Kit_left_arm_bvb1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4d/Kit_body_bvb1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1f/Kit_right_arm_bvb1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb1920e.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fb/Kit_socks_bvb1920e.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a></b>
</td></tr></tbody></table>
<h4><span id="Real_Madrid_.E2.80.93_Manchester_City"></span><span class="mw-headline" id="Real_Madrid_–_Manchester_City">Real Madrid – Manchester City</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=7" title="Editar sección: Real Madrid – Manchester City"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="RMA_MAN">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 26 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:2</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Santiago Bernabéu</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Isco" title="Isco">Isco</a> <span typeof="mw:File"><span title="Anotado en el minuto 60"><img alt="Anotado en el minuto 60" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">60'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027121/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 78"><img alt="Anotado en el minuto 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">78'</small> <a href="/wiki/Gabriel_Jesus" title="Gabriel Jesus">Gabriel Jesus</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 83"><img alt="Anotado en el minuto 83" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">83' </span> <a href="/wiki/Kevin_De_Bruyne" title="Kevin De Bruyne">De Bruyne</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 75&#160;615 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Daniele_Orsato" title="Daniele Orsato">Daniele Orsato</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a><br />Jugador del partido: <a href="/wiki/Kevin_De_Bruyne" title="Kevin De Bruyne">Kevin De Bruyne</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cb/Kit_left_arm_realmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d9/Kit_body_realmadrid1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_right_arm_realmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0d/Kit_shorts_realmadrid1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/a1/Kit_socks_realmadrid1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#84BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3a/Kit_left_arm_mancity1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#84BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/01/Kit_body_mancity1920a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#84BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/02/Kit_right_arm_mancity1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MAN_RMA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 7 de agosto de 2020, 21:00<sup id="cite_ref-ManchesterCityVSRealMadrid_3-0" class="reference separada"><a href="#cite_note-ManchesterCityVSRealMadrid-3"><span class="corchete-llamada">[</span>n. 1<span class="corchete-llamada">]</span></a></sup>&#8203;;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:1)</span></b> </div><div style="font-size: 85%">(Global <b>4:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a>,</span> <a href="/wiki/Manchester" class="mw-redirect" title="Manchester">Manchester</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Raheem_Sterling" title="Raheem Sterling">Sterling</a> <span typeof="mw:File"><span title="Anotado en el minuto 9"><img alt="Anotado en el minuto 9" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">9'</small></li>
<li><a href="/wiki/Gabriel_Jesus" title="Gabriel Jesus">Gabriel Jesus</a> <span typeof="mw:File"><span title="Anotado en el minuto 68"><img alt="Anotado en el minuto 68" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">68'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027131/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 27"><img alt="Anotado en el minuto 27" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">27'</small> <a href="/wiki/Karim_Benzema" title="Karim Benzema">Benzema</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 0 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Felix_Brych" title="Felix Brych">Felix Brych</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bastian_Dankert" title="Bastian Dankert">Bastian Dankert</a><br />Jugador del partido: <a href="/wiki/Kyle_Walker" title="Kyle Walker">Kyle Walker</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

<tr>
<td align="left" colspan="7" style="font-size:85%;text-align:left">Partido suspendido hasta nuevo aviso debido al brote del <a href="/wiki/SARS-CoV-2" title="SARS-CoV-2">Coronavirus-2 del Síndrome Respiratorio Agudo Grave</a> que afecta a numerosas partes del mundo.<sup id="cite_ref-4" class="reference separada"><a href="#cite_note-4"><span class="corchete-llamada">[</span>3<span class="corchete-llamada">]</span></a></sup>&#8203;
</td></tr></tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#77BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/70/Kit_left_arm_mancity2021h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#77BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5a/Kit_body_mancity2021h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#77BBFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/06/Kit_right_arm_mancity2021h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_mancity2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a6/Kit_shorts_mancity2021h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#77BBFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2021h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/cb/Kit_socks_mancity2021h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF8789"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid2021A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e1/Kit_left_arm_realmadrid2021A.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF8789"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid2021A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/01/Kit_body_realmadrid2021A.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF8789"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid2021A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_right_arm_realmadrid2021A.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF8789"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid2021A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/59/Kit_shorts_realmadrid2021A.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF8789"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid2021A.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b2/Kit_socks_realmadrid2021A.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td></tr></tbody></table>
<h4><span id="Atalanta_.E2.80.93_Valencia"></span><span class="mw-headline" id="Atalanta_–_Valencia">Atalanta – Valencia</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=8" title="Editar sección: Atalanta – Valencia"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="ATA_VAL">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 19 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Atalanta_Bergamasca_Calcio" title="Atalanta Bergamasca Calcio">Atalanta</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>4:1</b> (2:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Valencia_Club_de_F%C3%BAtbol" title="Valencia Club de Fútbol">Valencia</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">San Siro</a>,</span> <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Hans_Hateboer" title="Hans Hateboer">Hateboer</a> <span typeof="mw:File"><span title="Anotado en el minuto 16"><img alt="Anotado en el minuto 16" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">16'</small> <span typeof="mw:File"><span title="Anotado en el minuto 62"><img alt="Anotado en el minuto 62" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">62'</small></li>
<li><a href="/wiki/Josip_Ili%C4%8Di%C4%87" title="Josip Iličić">Iličić</a> <span typeof="mw:File"><span title="Anotado en el minuto 42"><img alt="Anotado en el minuto 42" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">42'</small></li>
<li><a href="/wiki/Remo_Freuler" title="Remo Freuler">Freuler</a> <span typeof="mw:File"><span title="Anotado en el minuto 57"><img alt="Anotado en el minuto 57" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">57'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027124/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 66"><img alt="Anotado en el minuto 66" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">66'</small> <a href="/wiki/Den%C3%ADs_Ch%C3%A9ryshev" title="Denís Chéryshev">Chéryshev</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 44&#160;236 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Michael_Oliver_(%C3%A1rbitro)" title="Michael Oliver (árbitro)">Michael Oliver</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/w/index.php?title=Christopher_Kavanagh&amp;action=edit&amp;redlink=1" class="new" title="Christopher Kavanagh (aún no redactado)">Christopher Kavanagh</a><br />Jugador del partido: <a href="/wiki/Hans_Hateboer" title="Hans Hateboer">Hans Hateboer</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_left_arm_atalanta1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_body_atalanta1920H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_right_arm_atalanta1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c0/Kit_shorts_atalanta1920H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atalanta1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/05/Kit_socks_atalanta1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/ce/Kit_left_arm_valenciacf1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d6/Kit_body_valenciacf1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_right_arm_valenciacf1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#F57710"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_valenciacf1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_shorts_valenciacf1920a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_valenciacf1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/d7/Kit_socks_valenciacf1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="VAL_ATA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 10 de marzo de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Valencia_Club_de_F%C3%BAtbol" title="Valencia Club de Fútbol">Valencia</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:4 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:2)</span></b> </div><div style="font-size: 85%">(Global <b>4:8</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Atalanta_Bergamasca_Calcio" title="Atalanta Bergamasca Calcio">Atalanta</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_de_Mestalla" title="Estadio de Mestalla">Mestalla</a>,</span> <a href="/wiki/Valencia" title="Valencia">Valencia</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Kevin_Gameiro" title="Kevin Gameiro">Gameiro</a> <span typeof="mw:File"><span title="Anotado en el minuto 21"><img alt="Anotado en el minuto 21" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">21'</small> <span typeof="mw:File"><span title="Anotado en el minuto 51"><img alt="Anotado en el minuto 51" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">51'</small></li>
<li><a href="/wiki/Ferran_Torres" title="Ferran Torres">Ferran Torres</a> <span typeof="mw:File"><span title="Anotado en el minuto 67"><img alt="Anotado en el minuto 67" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">67'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027134/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 3"><img alt="Anotado en el minuto 3" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">3' </span> <span typeof="mw:File"><span title="Anotado en el minuto 43"><img alt="Anotado en el minuto 43" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">43' </span> <span typeof="mw:File"><span title="Anotado en el minuto 71"><img alt="Anotado en el minuto 71" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">71'</small> <span typeof="mw:File"><span title="Anotado en el minuto 82"><img alt="Anotado en el minuto 82" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">82'</small> <a href="/wiki/Josip_Ili%C4%8Di%C4%87" title="Josip Iličić">Iličić</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 0 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Romania.svg" class="mw-file-description" title="Bandera de Rumania"><img alt="Bandera de Rumania" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/20px-Flag_of_Romania.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/30px-Flag_of_Romania.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/40px-Flag_of_Romania.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Ovidiu_Alin_Ha%C5%A3egan" class="mw-redirect" title="Ovidiu Alin Haţegan">Ovidiu Alin Haţegan</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Pawel_Gil" class="mw-redirect" title="Pawel Gil">Pawel Gil</a><br />Jugador del partido: <a href="/wiki/Josip_Ili%C4%8Di%C4%87" title="Josip Iličić">Josip Iličić</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

<tr>
<td align="left" colspan="7" style="font-size:85%;text-align:left">Partido disputado a puerta cerrada (sin público) debido al brote del <a href="/wiki/SARS-CoV-2" title="SARS-CoV-2">Coronavirus-2 del Síndrome Respiratorio Agudo Grave</a> que afecta a numerosas partes del mundo.<sup id="cite_ref-5" class="reference separada"><a href="#cite_note-5"><span class="corchete-llamada">[</span>4<span class="corchete-llamada">]</span></a></sup>&#8203;
</td></tr></tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/ce/Kit_left_arm_valenciacf1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d6/Kit_body_valenciacf1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_right_arm_valenciacf1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_valenciacf1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/68/Kit_shorts_valenciacf1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_valenciacf1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/d7/Kit_socks_valenciacf1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_left_arm_atalanta1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_body_atalanta1920H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atalanta1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_right_arm_atalanta1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atalanta1920A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_shorts_atalanta1920A.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atalanta1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/05/Kit_socks_atalanta1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Atalanta_Bergamasca_Calcio" title="Atalanta Bergamasca Calcio">Atalanta</a></b>
</td></tr></tbody></table>
<h4><span id="Atl.C3.A9tico_de_Madrid_.E2.80.93_Liverpool"></span><span class="mw-headline" id="Atlético_de_Madrid_–_Liverpool">Atlético de Madrid – Liverpool</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=9" title="Editar sección: Atlético de Madrid – Liverpool"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="ATM_LIV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 18 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0</b> (1:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Metropolitano_(Madrid)" title="Estadio Metropolitano (Madrid)">Wanda Metropolitano</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Sa%C3%BAl_%C3%91%C3%ADguez" title="Saúl Ñíguez">Saúl</a> <span typeof="mw:File"><span title="Anotado en el minuto 4"><img alt="Anotado en el minuto 4" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">4'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027125/index.html">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 67&#160;443 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Pawe%C5%82_Gil" title="Paweł Gil">Paweł Gil</a><br />Jugador del partido: <a href="/wiki/Renan_Lodi" title="Renan Lodi">Renan Lodi</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_left_arm_atlmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7e/Kit_body_atlmadrid1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/03/Kit_right_arm_atlmadrid1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atlmadrid1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b1/Kit_socks_atlmadrid1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c6/Kit_left_arm_liverpool1920t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_body_liverpool1920t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/40/Kit_right_arm_liverpool1920t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool1920t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/30/Kit_socks_liverpool1920t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LIV_ATM">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 11 de marzo de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:3 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:0, 1:0)</span></b> <span style="font-size: 85%">(<a href="/wiki/Pr%C3%B3rroga_(deporte)" title="Prórroga (deporte)">t.&#160;s.</a>)</span></div><div style="font-size: 85%">(<b>1:3</b> <a href="/wiki/Pr%C3%B3rroga_(deporte)" title="Prórroga (deporte)">t.&#160;s.</a>)</div><div style="font-size: 85%">(Global <b>2:4</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Anfield" title="Anfield">Anfield</a>,</span> <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Georginio_Wijnaldum" title="Georginio Wijnaldum">Wijnaldum</a> <span typeof="mw:File"><span title="Anotado en el minuto 43"><img alt="Anotado en el minuto 43" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">43'</small></li>
<li><a href="/wiki/Roberto_Firmino" title="Roberto Firmino">Firmino</a> <span typeof="mw:File"><span title="Anotado en el minuto 94"><img alt="Anotado en el minuto 94" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">94'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027135/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 97"><img alt="Anotado en el minuto 97" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">97'</small> <span typeof="mw:File"><span title="Anotado en el minuto 105&#39;+1"><img alt="Anotado en el minuto 105&#39;+1" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">105'+1'</small> <a href="/wiki/Marcos_Llorente" title="Marcos Llorente">Llorente</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 120&#39;+1"><img alt="Anotado en el minuto 120&#39;+1" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">120'+1'</small> <a href="/wiki/%C3%81lvaro_Morata" title="Álvaro Morata">Morata</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 52&#160;267 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Jochem_Kamphuis&amp;action=edit&amp;redlink=1" class="new" title="Jochem Kamphuis (aún no redactado)">Jochem Kamphuis</a><br />Jugador del partido: <a href="/wiki/Jan_Oblak" title="Jan Oblak">Jan Oblak</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/07/Kit_left_arm_liverpool1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fc/Kit_body_liverpool1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fa/Kit_right_arm_liverpool1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/cf/Kit_socks_liverpool1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/58/Kit_left_arm_atlmadrid1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/dc/Kit_body_atlmadrid1920a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/80/Kit_right_arm_atlmadrid1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atlmadrid1920a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/df/Kit_socks_atlmadrid1920a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a></b>
</td></tr></tbody></table>
<h4><span id="Chelsea_.E2.80.93_Bayern_de_M.C3.BAnich"></span><span class="mw-headline" id="Chelsea_–_Bayern_de_Múnich">Chelsea – Bayern de Múnich</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=10" title="Editar sección: Chelsea – Bayern de Múnich"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="CHE_BAY">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 25 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:3</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Stamford_Bridge_(estadio)" title="Stamford Bridge (estadio)">Stamford Bridge</a>,</span> <a href="/wiki/Londres" title="Londres">Londres</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027126/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 51"><img alt="Anotado en el minuto 51" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">51'</small> <span typeof="mw:File"><span title="Anotado en el minuto 54"><img alt="Anotado en el minuto 54" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">54'</small> <a href="/wiki/Serge_Gnabry" title="Serge Gnabry">Gnabry</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 76"><img alt="Anotado en el minuto 76" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">76'</small> <a href="/wiki/Robert_Lewandowski" title="Robert Lewandowski">Lewandowski</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 36&#160;761 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Cl%C3%A9ment_Turpin" title="Clément Turpin">Clément Turpin</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Fran%C3%A7ois_Letexier&amp;action=edit&amp;redlink=1" class="new" title="François Letexier (aún no redactado)">François Letexier</a><br />Jugador del partido: <a href="/wiki/Serge_Gnabry" title="Serge Gnabry">Serge Gnabry</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5b/Kit_left_arm_chelsea1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_body_chelsea1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cb/Kit_right_arm_chelsea1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_cfc201920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/95/Kit_shorts_cfc201920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/ca/Kit_socks_chelsea1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/12/Kit_left_arm_bayern1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/38/Kit_body_bayern1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_bayern1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#D50000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1b/Kit_shorts_bayern1920h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#D50000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_red.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_socks_3_stripes_red.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BAY_CHE">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 8 de agosto de 2020, 21:00<sup id="cite_ref-12demarzosuspensión_6-0" class="reference separada"><a href="#cite_note-12demarzosuspensión-6"><span class="corchete-llamada">[</span>n. 2<span class="corchete-llamada">]</span></a></sup>&#8203;;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>4:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(2:1)</span></b> </div><div style="font-size: 85%">(Global <b>7:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a>,</span> <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Robert_Lewandowski" title="Robert Lewandowski">Lewandowski</a> <span typeof="mw:File"><span title="Anotado en el minuto 9"><img alt="Anotado en el minuto 9" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">9' </span> <span typeof="mw:File"><span title="Anotado en el minuto 83"><img alt="Anotado en el minuto 83" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">83'</small></li>
<li><a href="/wiki/Ivan_Peri%C5%A1i%C4%87" title="Ivan Perišić">Perišić</a> <span typeof="mw:File"><span title="Anotado en el minuto 25"><img alt="Anotado en el minuto 25" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">25'</small></li>
<li><a href="/wiki/Corentin_Tolisso" title="Corentin Tolisso">Tolisso</a> <span typeof="mw:File"><span title="Anotado en el minuto 76"><img alt="Anotado en el minuto 76" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">76'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027132/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 44"><img alt="Anotado en el minuto 44" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">44'</small> <a href="/wiki/Tammy_Abraham" title="Tammy Abraham">Abraham</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 0 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Romania.svg" class="mw-file-description" title="Bandera de Rumania"><img alt="Bandera de Rumania" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/20px-Flag_of_Romania.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/30px-Flag_of_Romania.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/40px-Flag_of_Romania.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Ovidiu_Ha%C5%A3egan" title="Ovidiu Haţegan">Ovidiu Haţegan</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a><br />Jugador del partido: <a href="/wiki/Robert_Lewandowski" title="Robert Lewandowski">Robert Lewandowski</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/85/Kit_left_arm_bayern2021h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d5/Kit_body_bayern2021h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/28/Kit_right_arm_bayern2021h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidascondivo20rw.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bd/Kit_shorts_adidascondivo20rw.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/93/Kit_left_arm_chelsea2021h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3e/Kit_body_chelsea2021h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/53/Kit_right_arm_chelsea2021h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_chelsea2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2f/Kit_shorts_chelsea2021h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></b>
</td></tr></tbody></table>
<h4><span id="Olympique_de_Lyon_.E2.80.93_Juventus"></span><span class="mw-headline" id="Olympique_de_Lyon_–_Juventus">Olympique de Lyon – Juventus</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=11" title="Editar sección: Olympique de Lyon – Juventus"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LYO_JUV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 26 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0</b> (1:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Parc_Olympique_Lyonnais" title="Parc Olympique Lyonnais">Parc Olympique Lyonnais</a>,</span> <a href="/wiki/Lyon" title="Lyon">Lyon</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Lucas_Tousart" title="Lucas Tousart">Tousart</a> <span typeof="mw:File"><span title="Anotado en el minuto 31"><img alt="Anotado en el minuto 31" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">31'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027127/index.html">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 57&#160;335 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Jes%C3%BAs_Gil_Manzano" title="Jesús Gil Manzano">Jesús Gil Manzano</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Juan_Mart%C3%ADnez_Munuera" title="Juan Martínez Munuera">Juan Martínez Munuera</a><br />Jugador del partido: <a href="/wiki/Houssem_Aouar" title="Houssem Aouar">Houssem Aouar</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e0/Kit_left_arm_ol1920c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5d/Kit_body_ol1920c.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_right_arm_ol1920c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ol1920c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_shorts_ol1920c.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_lafc19A.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_socks_lafc19A.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0086CE"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_juventusfc1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5e/Kit_left_arm_juventusfc1920t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0086CE"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventusfc1920T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b3/Kit_body_juventusfc1920T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0086CE"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_juventusfc1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/47/Kit_right_arm_juventusfc1920t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0086CE"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_juventusfc1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_shorts_juventusfc1920t.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0086CE"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventusfc1920t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/34/Kit_socks_juventusfc1920t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="JUV_LYO">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 7 de agosto de 2020, 21:00<sup id="cite_ref-JuventusVSLyon_7-0" class="reference separada"><a href="#cite_note-JuventusVSLyon-7"><span class="corchete-llamada">[</span>n. 3<span class="corchete-llamada">]</span></a></sup>&#8203;;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:1)</span></b> </div><div style="font-size: 85%">(Global <b>2:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Juventus_Stadium" title="Juventus Stadium">Allianz Stadium</a>,</span> <a href="/wiki/Tur%C3%ADn" title="Turín">Turín</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Cristiano_Ronaldo" title="Cristiano Ronaldo">Ronaldo</a> <span typeof="mw:File"><span title="Anotado en el minuto 43"><img alt="Anotado en el minuto 43" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">43' </span> <span typeof="mw:File"><span title="Anotado en el minuto 60"><img alt="Anotado en el minuto 60" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">60'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027133/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 12"><img alt="Anotado en el minuto 12" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">12' </span> <a href="/wiki/Memphis_Depay" title="Memphis Depay">Depay</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 0 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Felix_Zwayer" title="Felix Zwayer">Felix Zwayer</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Christian_Dingert&amp;action=edit&amp;redlink=1" class="new" title="Christian Dingert (aún no redactado)">Christian Dingert</a><br />Jugador del partido: <a href="/wiki/Cristiano_Ronaldo" title="Cristiano Ronaldo">Cristiano Ronaldo</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

<tr>
<td align="left" colspan="7" style="font-size:85%;text-align:left">Partido suspendido hasta nuevo aviso debido al brote del <a href="/wiki/SARS-CoV-2" title="SARS-CoV-2">Coronavirus-2 del Síndrome Respiratorio Agudo Grave</a> que afecta a numerosas partes del mundo.<sup id="cite_ref-8" class="reference separada"><a href="#cite_note-8"><span class="corchete-llamada">[</span>5<span class="corchete-llamada">]</span></a></sup>&#8203;
</td></tr></tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_juventus2021H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7e/Kit_left_arm_juventus2021H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus2021H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2f/Kit_body_juventus2021H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_juventus2021H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2f/Kit_right_arm_juventus2021H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_juventus2021h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2f/Kit_shorts_juventus2021h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus2021h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/0a/Kit_socks_juventus2021h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#222222"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ol2021a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cf/Kit_left_arm_ol2021a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#222222"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ol2021a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/27/Kit_body_ol2021a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#222222"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ol2021a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/99/Kit_right_arm_ol2021a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidaswhite.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8e/Kit_shorts_adidaswhite.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_color_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/e3/Kit_socks_color_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a></b>
</td></tr></tbody></table>
<h4><span id="Tottenham_Hotspur_.E2.80.93_Leipzig"></span><span class="mw-headline" id="Tottenham_Hotspur_–_Leipzig">Tottenham Hotspur – Leipzig</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=12" title="Editar sección: Tottenham Hotspur – Leipzig"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="TOT_RBL">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 19 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:1</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Tottenham_Hotspur_Stadium" title="Tottenham Hotspur Stadium">Tottenham Hotspur Stadium</a>,</span> <a href="/wiki/Londres" title="Londres">Londres</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027122/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 58"><img alt="Anotado en el minuto 58" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">58' </span> <a href="/wiki/Timo_Werner" title="Timo Werner">Werner</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 60&#160;095 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/wiki/C%C3%BCneyt_%C3%87ak%C4%B1r" title="Cüneyt Çakır">Cüneyt Çakır</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/w/index.php?title=Mete_Kalkavan&amp;action=edit&amp;redlink=1" class="new" title="Mete Kalkavan (aún no redactado)">Mete Kalkavan</a><br />Jugador del partido: <a href="/wiki/Hugo_Lloris" title="Hugo Lloris">Hugo Lloris</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a1/Kit_left_arm_tottenham1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d3/Kit_body_tottenham1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/42/Kit_right_arm_tottenham1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/1/12/Kit_socks_tottenham1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0F0F0F"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0F0F0F"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rb1920t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ad/Kit_body_rb1920t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0F0F0F"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0F0F0F"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0F0F0F"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="RBL_TOT">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 10 de marzo de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(2:0)</span></b> </div><div style="font-size: 85%">(Global <b>4:0</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Red_Bull_Arena_(Leipzig)" title="Red Bull Arena (Leipzig)">Red Bull Arena</a>,</span> <a href="/wiki/Leipzig" title="Leipzig">Leipzig</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Marcel_Sabitzer" title="Marcel Sabitzer">Sabitzer</a> <span typeof="mw:File"><span title="Anotado en el minuto 10"><img alt="Anotado en el minuto 10" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">10'</small> <span typeof="mw:File"><span title="Anotado en el minuto 21"><img alt="Anotado en el minuto 21" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">21'</small></li>
<li><a href="/wiki/Emil_Forsberg" title="Emil Forsberg">Forsberg</a> <span typeof="mw:File"><span title="Anotado en el minuto 87"><img alt="Anotado en el minuto 87" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">87'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027128/index.html">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 42&#160;146 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Carlos_del_Cerro_Grande" title="Carlos del Cerro Grande">Carlos del Cerro Grande</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Juan_Mart%C3%ADnez_Munuera" title="Juan Martínez Munuera">Juan Martínez Munuera</a><br />Jugador del partido: <a href="/wiki/Marcel_Sabitzer" title="Marcel Sabitzer">Marcel Sabitzer</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_rbl1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/27/Kit_left_arm_rbl1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rblei1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_rblei1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_rbl1920H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9d/Kit_right_arm_rbl1920H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/93/Kit_left_arm_tottenham1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9c/Kit_body_tottenham1920a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/ce/Kit_right_arm_tottenham1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000040"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham1920a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_socks_tottenham1920a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a></b>
</td></tr></tbody></table>
<h4><span id="Napoli_.E2.80.93_Barcelona"></span><span class="mw-headline" id="Napoli_–_Barcelona">Napoli – Barcelona</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=13" title="Editar sección: Napoli – Barcelona"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="NAP_BAR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 25 de febrero de 2020, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Societa_Sportiva_Calcio_Napoli" class="mw-redirect" title="Societa Sportiva Calcio Napoli">Napoli</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:1</b> (1:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_San_Paolo" class="mw-redirect" title="Estadio San Paolo">Estadio San Paolo</a>,</span> <a href="/wiki/N%C3%A1poles" title="Nápoles">Nápoles</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Dries_Mertens" title="Dries Mertens">Mertens</a>   <span typeof="mw:File"><span title="Anotado en el minuto 30"><img alt="Anotado en el minuto 30" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">30'</small></li></ul>
</td>
<td valign="top" align="center">
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 57"><img alt="Anotado en el minuto 57" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">57'</small> <a href="/wiki/Antoine_Griezmann" title="Antoine Griezmann">Griezmann</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 44&#160;348 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Felix_Brych" title="Felix Brych">Felix Brych</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bastian_Dankert" title="Bastian Dankert">Bastian Dankert</a><br />Jugador del partido: <a href="/wiki/Sergio_Busquets" title="Sergio Busquets">Sergio Busquets</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/10/Kit_left_arm_napoli1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/29/Kit_body_napoli1920e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_right_arm_napoli1920e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#ffffff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_napoli1920e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/40/Kit_shorts_napoli1920e.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#ffffff"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_napoli1920H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/2/29/Kit_socks_napoli1920H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFDD00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcbarcelona1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/54/Kit_left_arm_fcbarcelona1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFDD00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcbarcelona1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/90/Kit_body_fcbarcelona1920a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFDD00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcbarcelona1920a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/08/Kit_right_arm_fcbarcelona1920a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFDD00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFDD00"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbarcelona1920a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4a/Kit_socks_fcbarcelona1920a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BAR_NAP">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 8 de agosto de 2020, 21:00<sup id="cite_ref-12demarzosuspensión_6-1" class="reference separada"><a href="#cite_note-12demarzosuspensión-6"><span class="corchete-llamada">[</span>n. 2<span class="corchete-llamada">]</span></a></sup>&#8203;;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(3:1)</span></b> </div><div style="font-size: 85%">(Global <b>4:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Societa_Sportiva_Calcio_Napoli" class="mw-redirect" title="Societa Sportiva Calcio Napoli">Napoli</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Camp_Nou" title="Camp Nou">Camp Nou</a>,</span> <a href="/wiki/Barcelona" title="Barcelona">Barcelona</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Cl%C3%A9ment_Lenglet" title="Clément Lenglet">Lenglet</a> <span typeof="mw:File"><span title="Anotado en el minuto 10"><img alt="Anotado en el minuto 10" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">10'</small></li>
<li><a href="/wiki/Lionel_Messi" title="Lionel Messi">Messi</a> <span typeof="mw:File"><span title="Anotado en el minuto 23"><img alt="Anotado en el minuto 23" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">23'</small></li>
<li><a href="/wiki/Luis_Su%C3%A1rez_(futbolista)" title="Luis Suárez (futbolista)">Suárez</a> <span typeof="mw:File"><span title="Anotado en el minuto 45+1"><img alt="Anotado en el minuto 45+1" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">45+1' </span></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://www.uefa.com/uefachampionsleague/season=2020/matches/round=2001141/match=2027129/index.html">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 45+5"><img alt="Anotado en el minuto 45+5" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">45+5' </span> <a href="/wiki/Lorenzo_Insigne" title="Lorenzo Insigne">Insgine</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 0 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/wiki/C%C3%BCneyt_%C3%87ak%C4%B1r" title="Cüneyt Çakır">Cüneyt Çakır</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/w/index.php?title=Mete_Kalkavan&amp;action=edit&amp;redlink=1" class="new" title="Mete Kalkavan (aún no redactado)">Mete Kalkavan</a><br />Jugador del partido: <a href="/wiki/Lionel_Messi" title="Lionel Messi">Lionel Messi</a> <span typeof="mw:File"><span title="Jugador del partido"><img alt="Jugador del partido" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/15px-Star_Ouro.svg.png" decoding="async" width="15" height="14" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/23px-Star_Ouro.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Star_Ouro.svg/30px-Star_Ouro.svg.png 2x" data-file-width="750" data-file-height="706" /></span></span>
</td></tr>

<tr>
<td align="left" colspan="7" style="font-size:85%;text-align:left">Partido disputado a puerta cerrada (sin público) debido al brote del <a href="/wiki/SARS-CoV-2" title="SARS-CoV-2">Coronavirus-2 del Síndrome Respiratorio Agudo Grave</a> que afecta a numerosas partes del mundo.<sup id="cite_ref-9" class="reference separada"><a href="#cite_note-9"><span class="corchete-llamada">[</span>6<span class="corchete-llamada">]</span></a></sup>&#8203;
</td></tr></tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcbarcelona1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_left_arm_fcbarcelona1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcbarcelona1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/da/Kit_body_fcbarcelona1920h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcbarcelona1920h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9a/Kit_right_arm_fcbarcelona1920h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000080"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000080"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_barcelona1920h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_socks_barcelona1920h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_napoli1920te.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_napoli1920te.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_napoli1920te.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cd/Kit_body_napoli1920te.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_napoli1920te.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d7/Kit_right_arm_napoli1920te.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_napoli1920te.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b1/Kit_shorts_napoli1920te.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#ffffff"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_napoli1920A.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/ff/Kit_socks_napoli1920A.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></b>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Clasificados_para_cuartos_de_final">Clasificados para cuartos de final</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=14" title="Editar sección: Clasificados para cuartos de final"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table align="center" cellpadding="2" cellspacing="0" style="background: #f5faff; border: 1px #aaa solid; border-collapse: collapse; font-size: 95%;" width="80%">

<tbody><tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/45px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/68px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/45px-Flag_of_Italy.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/68px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Manchester_City" class="mw-redirect" title="Manchester City">Manchester City</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Atalanta_Bergamasca_Calcio" title="Atalanta Bergamasca Calcio">Atalanta</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a></b>
</td></tr>
<tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/45px-Flag_of_Germany.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/68px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/45px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/68px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/45px-Flag_of_Germany.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/68px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern de Múnich</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></b>
</td></tr></tbody></table>
<h2><span id="V.C3.A9ase_tambi.C3.A9n"></span><span class="mw-headline" id="Véase_también">Véase también</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=15" title="Editar sección: Véase también"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/Anexo:Ronda_preliminar_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Ronda preliminar de la Liga de Campeones de la UEFA 2019-20">Anexo: Ronda preliminar de la Liga de Campeones de la UEFA 2019-20</a></li>
<li><a href="/wiki/Anexo:Primera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Primera ronda previa de la Liga de Campeones de la UEFA 2019-20">Anexo: Primera ronda previa de la Liga de Campeones de la UEFA 2019-20</a></li>
<li><a href="/wiki/Anexo:Segunda_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Segunda ronda previa de la Liga de Campeones de la UEFA 2019-20">Anexo: Segunda ronda previa de la Liga de Campeones de la UEFA 2019-20</a></li>
<li><a href="/wiki/Anexo:Tercera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Tercera ronda previa de la Liga de Campeones de la UEFA 2019-20">Anexo: Tercera ronda previa de la Liga de Campeones de la UEFA 2019-20</a></li>
<li><a href="/wiki/Anexo:Cuarta_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Cuarta ronda previa de la Liga de Campeones de la UEFA 2019-20">Anexo: Cuarta ronda previa de la Liga de Campeones de la UEFA 2019-20</a></li>
<li>Fase de grupos <small>(<a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2019-20">Grupo A</a>, <a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2019-20">Grupo B</a>, <a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2019-20">Grupo C</a>, <a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2019-20">Grupo D</a>, <a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2019-20">Grupo E</a>, <a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2019-20">Grupo F</a>, <a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2019-20">Grupo G</a>, <a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2019-20">Grupo H</a>)</small></li>
<li><a href="/wiki/Anexo:Cuartos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Cuartos de final de la Liga de Campeones de la UEFA 2019-20">Anexo: Cuartos de final de la Liga de Campeones de la UEFA 2019-20</a></li>
<li><a href="/wiki/Anexo:Semifinales_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Semifinales de la Liga de Campeones de la UEFA 2019-20">Anexo: Semifinales de la Liga de Campeones de la UEFA 2019-20</a></li>
<li><a href="/wiki/Final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Final de la Liga de Campeones de la UEFA 2019-20">Final de la Liga de Campeones de la UEFA 2019-20</a></li></ul>
<h2><span class="mw-headline" id="Enlaces_externos">Enlaces externos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=16" title="Editar sección: Enlaces externos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://es.uefa.com">Página oficial de la UEFA</a></li>
<li><a rel="nofollow" class="external text" href="http://es.uefa.com/uefachampionsleague/index.html">Página oficial de la UEFA Champions League</a></li></ul>
<h2><span class="mw-headline" id="Referencias">Referencias</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;action=edit&amp;section=17" title="Editar sección: Referencias"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="listaref" style="list-style-type: decimal;"><ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><a href="#cite_ref-1">↑</a></span> <span class="reference-text"><span id="CITAREFDiario_As" class="citation web">Diario <i>As</i> (ed.). <a rel="nofollow" class="external text" href="https://as.com/futbol/2020/03/08/internacional/1583705636_454362.html?m1=cG9ydGFkYV9wb3J0YWRh&amp;m2=QUNUVUFMSURBRA%3D%3D&amp;m3=Mg%3D%3D&amp;m4=dmlkZW8%3D&amp;m5=MjE%3D">«Oficial: el PSG-Dortmund también se jugará a puerta cerrada»</a><span class="reference-accessdate">. Consultado el 9 de marzo de 2020</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20&amp;rft.btitle=Oficial%3A+el+PSG-Dortmund+tambi%C3%A9n+se+jugar%C3%A1+a+puerta+cerrada&amp;rft.genre=book&amp;rft_id=https%3A%2F%2Fas.com%2Ffutbol%2F2020%2F03%2F08%2Finternacional%2F1583705636_454362.html%3Fm1%3DcG9ydGFkYV9wb3J0YWRh%26m2%3DQUNUVUFMSURBRA%253D%253D%26m3%3DMg%253D%253D%26m4%3DdmlkZW8%253D%26m5%3DMjE%253D&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-Actualizacióndel12demarzo-2"><span class="mw-cite-backlink">↑ <a href="#cite_ref-Actualizacióndel12demarzo_2-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-Actualizacióndel12demarzo_2-1"><sup><i><b>b</b></i></sup></a></span> <span class="reference-text"><span id="CITAREFUEFA12_de_marzo_de_2020" class="citation web">UEFA (12 de marzo de 2020). <a rel="nofollow" class="external text" href="https://www.uefa.com/insideuefa/news/newsid=2640915.html">«Update on UEFA competition matches (12 March 2020)» &#91;Actualización sobre los partidos de la competición de la UEFA (12 de marzo de 2020)&#93;</a> <span style="color:#555;">(en inglés)</span><span class="reference-accessdate">. Consultado el 12 de marzo de 2020</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20&amp;rft.au=UEFA&amp;rft.aulast=UEFA&amp;rft.btitle=Update+on+UEFA+competition+matches+%2812+March+2020%29&amp;rft.date=12+de+marzo+de+2020&amp;rft.genre=book&amp;rft_id=https%3A%2F%2Fwww.uefa.com%2Finsideuefa%2Fnews%2Fnewsid%3D2640915.html&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-4"><span class="mw-cite-backlink"><a href="#cite_ref-4">↑</a></span> <span class="reference-text"><span id="CITAREFDiario_El_Mundo" class="citation web">Diario <i>El Mundo</i> (ed.). <a rel="nofollow" class="external text" href="https://www.elmundo.es/deportes/futbol/champions-league/2020/03/12/5e6a5e17fdddff2b418b4718.html">«Aplazado el Manchester City - Real Madrid de Champions por el coronavirus»</a><span class="reference-accessdate">. Consultado el 12 de marzo de 2020</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20&amp;rft.btitle=Aplazado+el+Manchester+City+-+Real+Madrid+de+Champions+por+el+coronavirus&amp;rft.genre=book&amp;rft_id=https%3A%2F%2Fwww.elmundo.es%2Fdeportes%2Ffutbol%2Fchampions-league%2F2020%2F03%2F12%2F5e6a5e17fdddff2b418b4718.html&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-5"><span class="mw-cite-backlink"><a href="#cite_ref-5">↑</a></span> <span class="reference-text"><span id="CITAREFDiario_As" class="citation web">Diario <i>As</i> (ed.). <a rel="nofollow" class="external text" href="https://as.com/futbol/2020/03/04/champions/1583348516_754761.html">«Sanidad confirma que el Valencia-Atalanta se jugará a puerta cerrada»</a><span class="reference-accessdate">. Consultado el 5 de marzo de 2020</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20&amp;rft.btitle=Sanidad+confirma+que+el+Valencia-Atalanta+se+jugar%C3%A1+a+puerta+cerrada&amp;rft.genre=book&amp;rft_id=https%3A%2F%2Fas.com%2Ffutbol%2F2020%2F03%2F04%2Fchampions%2F1583348516_754761.html&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-8"><span class="mw-cite-backlink"><a href="#cite_ref-8">↑</a></span> <span class="reference-text"><span id="CITAREFUEFA" class="citation web"><a href="/wiki/UEFA" title="UEFA">UEFA</a> (ed.). <a rel="nofollow" class="external text" href="https://es.uefa.com/insideuefa/news/newsid=2640916.html">«Actualización sobre partidos de competición UEFA (12 de marzo de 2020)»</a><span class="reference-accessdate">. Consultado el 12 de marzo de 2020</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20&amp;rft.btitle=Actualizaci%C3%B3n+sobre+partidos+de+competici%C3%B3n+UEFA+%2812+de+marzo+de+2020%29&amp;rft.genre=book&amp;rft_id=https%3A%2F%2Fes.uefa.com%2Finsideuefa%2Fnews%2Fnewsid%3D2640916.html&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-9"><span class="mw-cite-backlink"><a href="#cite_ref-9">↑</a></span> <span class="reference-text"><span id="CITAREFDiario_Marca" class="citation web">Diario <i>Marca</i> (ed.). <a rel="nofollow" class="external text" href="https://www.marca.com/futbol/barcelona/2020/03/10/5e676220e2704ecda18b45ef.html">«El Barcelona - Nápoles se jugará a puerta cerrada»</a><span class="reference-accessdate">. Consultado el 10 de marzo de 2020</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2019-20&amp;rft.btitle=El+Barcelona+-+N%C3%A1poles+se+jugar%C3%A1+a+puerta+cerrada&amp;rft.genre=book&amp;rft_id=https%3A%2F%2Fwww.marca.com%2Ffutbol%2Fbarcelona%2F2020%2F03%2F10%2F5e676220e2704ecda18b45ef.html&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
</ol></div>
<div class="listaref" style="list-style-type: decimal;"><ol class="references">
<li id="cite_note-ManchesterCityVSRealMadrid-3"><span class="mw-cite-backlink"><a href="#cite_ref-ManchesterCityVSRealMadrid_3-0">↑</a></span> <span class="reference-text">El partido Manchester City vs Real Madrid, originalmente fue programado para el 17 de marzo de 2020, 21:00 CET (20:00 GMT) en Manchester, se pospuso indefinidamente ya que los jugadores del Real Madrid fueron puestos en cuarentena debido a la <a href="/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Espa%C3%B1a" class="mw-redirect" title="Pandemia de enfermedad por coronavirus de 2020 en España">pandemia de COVID-19 en España</a>.<sup id="cite_ref-Actualizacióndel12demarzo_2-0" class="reference separada"><a href="#cite_note-Actualizacióndel12demarzo-2"><span class="corchete-llamada">[</span>2<span class="corchete-llamada">]</span></a></sup>&#8203;</span>
</li>
<li id="cite_note-12demarzosuspensión-6"><span class="mw-cite-backlink">↑ <a href="#cite_ref-12demarzosuspensión_6-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-12demarzosuspensión_6-1"><sup><i><b>b</b></i></sup></a></span> <span class="reference-text">Los últimos dos partidos de 16 partidos, (entre Bayern Múnich vs. Chelsea y FC Barcelona vs Napoli), originalmente estaban programados para jugarse el 18 de marzo de 2020, 21:00 CET, se pospuso indefinidamente después de la suspensión de las competiciones de la UEFA debido a la pandemia de <a href="/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Europa" class="mw-redirect" title="Pandemia de enfermedad por coronavirus de 2020 en Europa">COVID-19 en Europa</a>.</span>
</li>
<li id="cite_note-JuventusVSLyon-7"><span class="mw-cite-backlink"><a href="#cite_ref-JuventusVSLyon_7-0">↑</a></span> <span class="reference-text">El partido Juventus vs. Olympique Lyonnais, originalmente fue programado para jugarse el 17 de marzo de 2020, 21:00 CET en Turín, se pospuso indefinidamente ya que los jugadores de la Juventus fueron puestos en cuarentena debido a la <a href="/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Italia" class="mw-redirect" title="Pandemia de enfermedad por coronavirus de 2020 en Italia">pandemia de COVID-19 en Italia</a>.<sup id="cite_ref-Actualizacióndel12demarzo_2-1" class="reference separada"><a href="#cite_note-Actualizacióndel12demarzo-2"><span class="corchete-llamada">[</span>2<span class="corchete-llamada">]</span></a></sup>&#8203;</span>
</li>
</ol></div>
<p><br clear="all" />
</p>
<table class="wikitable" border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; margin:0 auto;">

<tbody><tr style="text-align: center;">
<td width="30%">Predecesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2018-19">2018-19</a></b>
</td>
<td width="40%"><b>Octavos de final de la<br /><a href="/wiki/Liga_de_Campeones_de_la_UEFA" title="Liga de Campeones de la UEFA">Liga de Campeones de la UEFA</a></b><br />2019-20
</td>
<td width="30%">Sucesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2020-21" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2020-21">2020-21</a></b>
</td></tr></tbody></table>
<!-- 
NewPP limit report
Parsed by mw‐api‐int.codfw.main‐774c7d5bcb‐2gksx
Cached time: 20240212175259
Cache expiry: 2592000
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.829 seconds
Real time usage: 1.019 seconds
Preprocessor visited node count: 25794/1000000
Post‐expand include size: 280216/2097152 bytes
Template argument size: 102145/2097152 bytes
Highest expansion depth: 14/100
Expensive parser function count: 0/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 12233/5000000 bytes
Lua time usage: 0.079/10.000 seconds
Lua memory usage: 2545981/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  471.216      1 -total
 61.04%  287.622     16 Plantilla:Partidos
 16.91%   79.679     64 Plantilla:En_varias_líneas
 15.78%   74.353     88 Plantilla:Bandera
 10.24%   48.232      2 Plantilla:Listaref
  8.10%   38.154      6 Plantilla:Cita_web
  7.82%   36.855     16 Plantilla:Str_sub
  7.59%   35.756     32 Plantilla:Trim
  7.49%   35.290    128 Plantilla:Bandera_icono
  7.34%   34.567     32 Plantilla:Árbitro
-->

<!-- Saved in parser cache with key eswiki:pcache:idhash:9207107-0!canonical and timestamp 20240212175258 and revision id 154476111. Rendering was triggered because: api-parse
 -->
</div><!--esi <esi:include src="/esitest-fa8a495983347898/content" /> --><noscript><img src="https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" width="1" height="1" style="border: none; position: absolute;"></noscript>
<div class="printfooter" data-nosnippet="">Obtenido de «<a dir="ltr" href="https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;oldid=154476111">https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;oldid=154476111</a>»</div></div>
					<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Especial:Categor%C3%ADas" title="Especial:Categorías">Categoría</a>: <ul><li><a href="/wiki/Categor%C3%ADa:Liga_de_Campeones_de_la_UEFA_2019-20" title="Categoría:Liga de Campeones de la UEFA 2019-20">Liga de Campeones de la UEFA 2019-20</a></li></ul></div></div>
				</div>
			</main>
			
		</div>
		<div class="mw-footer-container">
			
<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info">
	<li id="footer-info-lastmod"> Esta página se editó por última vez el 9 oct 2023 a las 18:18.</li>
	<li id="footer-info-copyright">El texto está disponible bajo la <a rel="license" href="https://es.wikipedia.org/wiki/Wikipedia:Texto_de_la_Licencia_Creative_Commons_Atribuci%C3%B3n-CompartirIgual_4.0_Internacional">Licencia Creative Commons Atribución-CompartirIgual 4.0</a><a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es" style="display:none;"></a>; pueden aplicarse cláusulas adicionales. Al usar este sitio aceptas nuestros <a href="https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/es">términos de uso</a> y nuestra <a href="https://foundation.wikimedia.org/wiki/Policy:Privacy_policy/es">política de privacidad</a>.<br/>Wikipedia&reg; es una marca registrada de la <a href="https://wikimediafoundation.org/es/">Fundación Wikimedia</a>, una organización sin ánimo de lucro.</li>
</ul>

	<ul id="footer-places">
	<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy/es">Política de privacidad</a></li>
	<li id="footer-places-about"><a href="/wiki/Wikipedia:Acerca_de">Acerca de Wikipedia</a></li>
	<li id="footer-places-disclaimers"><a href="/wiki/Wikipedia:Limitaci%C3%B3n_general_de_responsabilidad">Limitación de responsabilidad</a></li>
	<li id="footer-places-wm-codeofconduct"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct">Código de conducta</a></li>
	<li id="footer-places-developers"><a href="https://developer.wikimedia.org">Desarrolladores</a></li>
	<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/es.wikipedia.org">Estadísticas</a></li>
	<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement/es">Declaración de cookies</a></li>
	<li id="footer-places-mobileview"><a href="//es.m.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Versión para móviles</a></li>
</ul>

	<ul id="footer-icons" class="noprint">
	<li id="footer-copyrightico"><a href="https://wikimediafoundation.org/"><img src="/static/images/footer/wikimedia-button.png" srcset="/static/images/footer/wikimedia-button-1.5x.png 1.5x, /static/images/footer/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation" loading="lazy" /></a></li>
	<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img src="/static/images/footer/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/footer/poweredby_mediawiki_132x47.png 1.5x, /static/images/footer/poweredby_mediawiki_176x62.png 2x" width="88" height="31" loading="lazy"></a></li>
</ul>

</footer>

		</div>
	</div> 
</div> 
<div class="vector-settings" id="p-dock-bottom">
	<ul>
		<li>
		<button class="cdx-button cdx-button--icon-only vector-limited-width-toggle" id=""><span class="vector-icon mw-ui-icon-fullScreen mw-ui-icon-wikimedia-fullScreen"></span>

<span>Activar o desactivar el límite de anchura del contenido</span>
</button>
</li>
	</ul>
</div>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgHostname":"mw1454","wgBackendResponseTime":126,"wgPageParseReport":{"limitreport":{"cputime":"0.829","walltime":"1.019","ppvisitednodes":{"value":25794,"limit":1000000},"postexpandincludesize":{"value":280216,"limit":2097152},"templateargumentsize":{"value":102145,"limit":2097152},"expansiondepth":{"value":14,"limit":100},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":1,"limit":20},"unstrip-size":{"value":12233,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  471.216      1 -total"," 61.04%  287.622     16 Plantilla:Partidos"," 16.91%   79.679     64 Plantilla:En_varias_líneas"," 15.78%   74.353     88 Plantilla:Bandera"," 10.24%   48.232      2 Plantilla:Listaref","  8.10%   38.154      6 Plantilla:Cita_web","  7.82%   36.855     16 Plantilla:Str_sub","  7.59%   35.756     32 Plantilla:Trim","  7.49%   35.290    128 Plantilla:Bandera_icono","  7.34%   34.567     32 Plantilla:Árbitro"]},"scribunto":{"limitreport-timeusage":{"value":"0.079","limit":"10.000"},"limitreport-memusage":{"value":2545981,"limit":52428800}},"cachereport":{"origin":"mw-api-int.codfw.main-774c7d5bcb-2gksx","timestamp":"20240212175259","ttl":2592000,"transientcontent":false}}});});</script>
</body>
</html>"""

#Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
tabla = soup.find('table', {'class': 'wikitable', 'style': 'text-align:center'})

#Verificamos si esta
if tabla:
    #Obtener todas las filas y celdas de la tabla
	rows = tabla.find_all('tr')

	#Crear una lista para almacenas las filas de datos
	tabla_data = []

	#Recorrer cada fila y extraer el texto de las celdas
	for i, row in enumerate(rows):
		# Omitir la primera iteración (i == 0) para evitar la primera fila de nombres de columnas
		if i == 0:
			continue
		cells = row.find_all(['td', 'th'])
		row_data = [cell.get_text(strip=True) for cell in cells]
		row_data.append('19/20')
			
		tabla_data.append(row_data)

	#Especicificar nombre del csv donde guardar la tabla
	file_name = 'octavos.csv'
	with open(file_name, 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(tabla_data)
	print(f'Se guardó la tabla en {file_name}')

else:
	print('No se encontró la tabla')