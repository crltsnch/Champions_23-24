from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import csv

#Obtener tabla de partidos de octavos del contenido de wikipedia

html = """<!DOCTYPE html>
<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available" lang="es" dir="ltr">
<head>
<meta charset="UTF-8">
<title>Anexo:Octavos de final de la Liga de Campeones de la UEFA 2021-22 - Wikipedia, la enciclopedia libre</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available";var cookie=document.cookie.match(/(?:^|; )eswikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":[",\t."," \t,"],
"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],"wgRequestId":"3f94dd7b-0b55-4701-a64f-d4005851129d","wgCanonicalNamespace":"Anexo","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":104,"wgPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22","wgTitle":"Octavos de final de la Liga de Campeones de la UEFA 2021-22","wgCurRevisionId":149436018,"wgRevisionId":149436018,"wgArticleId":9710387,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Liga de Campeones de la UEFA 2021-22"],"wgPageViewLanguage":"es","wgPageContentLanguage":"es","wgPageContentModel":"wikitext","wgRelevantPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22","wgRelevantArticleId":9710387,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,
"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoticeProject":"wikipedia","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsFlags":6,"wgVisualEditor":{"pageLanguageCode":"es","pageLanguageDir":"ltr","pageVariantFallbacks":"es"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":true,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":50000,"wgULSCurrentAutonym":"español","wgCentralAuthMobileDomain":false,"wgEditSubmitButtonLabelPublish":true,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,"wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgCheckUserClientHintsHeadersJsApi":["architecture","bitness","brands","fullVersionList","mobile","model","platform","platformVersion"],"GEHomepageSuggestedEditsEnableTopics":true,"wgGETopicsMatchModeEnabled":true,"wgGEStructuredTaskRejectionReasonTextInputEnabled":false,"wgGELevelingUpEnabledForUser":false};RLSTATE={
"skins.vector.user.styles":"ready","ext.gadget.imagenesinfobox":"ready","ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","skins.vector.user":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","codex-search-styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","wikibase.client.init":"ready","ext.wikimediaBadges":"ready"};RLPAGEMODULES=["mediawiki.toggleAllCollapsibles","site","mediawiki.page.ready","mediawiki.toc","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.a-commons-directo","ext.gadget.ReferenceTooltips","ext.gadget.refToolbar","ext.gadget.switcher","ext.urlShortener.toolbar","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.echo.centralauth","ext.eventLogging",
"ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.cx.uls.quick.actions","ext.checkUser.clientHints"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
}];});});</script>
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=codex-search-styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cskins.vector.icons%2Cstyles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector-2022">
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
<meta property="og:title" content="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2021-22 - Wikipedia, la enciclopedia libre">
<meta property="og:type" content="website">
<link rel="preconnect" href="//upload.wikimedia.org">
<link rel="alternate" media="only screen and (max-width: 720px)" href="//es.m.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22">
<link rel="alternate" type="application/x-wiki" title="Editar" href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">
<link rel="icon" href="/static/favicon/wikipedia.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (es)">
<link rel="EditURI" type="application/rsd+xml" href="//es.wikipedia.org/w/api.php?action=rsd">
<link rel="canonical" href="https://es.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">
<link rel="alternate" type="application/atom+xml" title="Canal Atom de Wikipedia" href="/w/index.php?title=Especial:CambiosRecientes&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="//login.wikimedia.org">
</head>
<body class="skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-104 ns-subject mw-editable page-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22 rootpage-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22 skin-vector-2022 action-view"><a class="mw-jump-link" href="#bodyContent">Ir al contenido</a>
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
			<li id="pt-createaccount-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2021-22" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio" class=""><span>Crear una cuenta</span></a>
</li>
<li id="pt-login-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2021-22" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o" class=""><span>Acceder</span></a>
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
			
			<li id="pt-createaccount" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2021-22" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio"><span class="vector-icon mw-ui-icon-userAdd mw-ui-icon-wikimedia-userAdd"></span> <span>Crear una cuenta</span></a></li><li id="pt-login" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2021-22" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o"><span class="vector-icon mw-ui-icon-logIn mw-ui-icon-wikimedia-logIn"></span> <span>Acceder</span></a></li>
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
			<li id="toc-Salzburgo_–_Bayern_Múnich"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Salzburgo_–_Bayern_Múnich">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.1</span>Salzburgo – Bayern Múnich</div>
			</a>
			
			<ul id="toc-Salzburgo_–_Bayern_Múnich-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Sporting_de_Portugal_–_Manchester_City"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Sporting_de_Portugal_–_Manchester_City">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.2</span>Sporting de Portugal – Manchester City</div>
			</a>
			
			<ul id="toc-Sporting_de_Portugal_–_Manchester_City-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Benfica_–_Ajax"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Benfica_–_Ajax">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.3</span>Benfica – Ajax</div>
			</a>
			
			<ul id="toc-Benfica_–_Ajax-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Chelsea_–_Lille"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Chelsea_–_Lille">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.4</span>Chelsea – Lille</div>
			</a>
			
			<ul id="toc-Chelsea_–_Lille-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Atlético_de_Madrid_–_Manchester_United"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Atlético_de_Madrid_–_Manchester_United">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.5</span>Atlético de Madrid – Manchester United</div>
			</a>
			
			<ul id="toc-Atlético_de_Madrid_–_Manchester_United-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Villarreal_–_Juventus"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Villarreal_–_Juventus">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.6</span>Villarreal – Juventus</div>
			</a>
			
			<ul id="toc-Villarreal_–_Juventus-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Inter_de_Milán_–_Liverpool"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Inter_de_Milán_–_Liverpool">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.7</span>Inter de Milán – Liverpool</div>
			</a>
			
			<ul id="toc-Inter_de_Milán_–_Liverpool-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-París_Saint-Germain_–_Real_Madrid"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#París_Saint-Germain_–_Real_Madrid">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.8</span>París Saint-Germain – Real Madrid</div>
			</a>
			
			<ul id="toc-París_Saint-Germain_–_Real_Madrid-sublist" class="vector-toc-list">
			</ul>
		</li>
	</ul>
	</li>
	<li id="toc-Clasificados_para_Cuartos_de_final"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Clasificados_para_Cuartos_de_final">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">6</span>Clasificados para Cuartos de final</div>
		</a>
		
		<ul id="toc-Clasificados_para_Cuartos_de_final-sublist" class="vector-toc-list">
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
	<li id="toc-Referencias"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Referencias">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">8</span>Referencias</div>
		</a>
		
		<ul id="toc-Referencias-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Enlaces_externos"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Enlaces_externos">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">9</span>Enlaces externos</div>
		</a>
		
		<ul id="toc-Enlaces_externos-sublist" class="vector-toc-list">
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
					<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-namespace">Anexo</span><span class="mw-page-title-separator">:</span><span class="mw-page-title-main">Octavos de final de la Liga de Campeones de la UEFA 2021-22</span></h1>
							
<div id="p-lang-btn" class="vector-dropdown mw-portlet mw-portlet-lang"  >
	<input type="checkbox" id="p-lang-btn-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-lang-btn" class="vector-dropdown-checkbox mw-interlanguage-selector" aria-label="Este artículo existe sólo en este idioma. Añade el artículo para otros idiomas"   >
	<label id="p-lang-btn-label" for="p-lang-btn-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--action-progressive mw-portlet-lang-heading-0" aria-hidden="true"  ><span class="vector-icon mw-ui-icon-language-progressive mw-ui-icon-wikimedia-language-progressive"></span>

<span class="vector-dropdown-label-text">Añadir idiomas</span>
	</label>
	<div class="vector-dropdown-content">

		<div class="vector-menu-content">
			
			<ul class="vector-menu-content-list">
				
				
			</ul>
			<div class="after-portlet after-portlet-lang"><span class="uls-after-portlet-link"></span><span class="wb-langlinks-add wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:NewItem?site=eswiki&amp;page=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2021-22" title="Agregar enlaces interlingüísticos" class="wbc-editpage">Añadir enlaces</a></span></div>
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
			
			<li id="ca-nstab-anexo" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Ver la página de contenido [c]" accesskey="c"><span>Anexo</span></a></li><li id="ca-talk" class="new vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo_discusi%C3%B3n:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;redlink=1" rel="discussion" title="Discusión acerca de la página (aún no redactado) [t]" accesskey="t"><span>Discusión</span></a></li>
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
			
			<li id="ca-view" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22"><span>Leer</span></a></li><li id="ca-edit" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-history" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=history" title="Versiones anteriores de esta página [h]" accesskey="h"><span>Ver historial</span></a></li>
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
			
			<li id="ca-more-view" class="selected vector-more-collapsible-item mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22"><span>Leer</span></a></li><li id="ca-more-edit" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-more-history" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=history"><span>Ver historial</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-tb" class="vector-menu mw-portlet mw-portlet-tb"  >
	<div class="vector-menu-heading">
		General
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-whatlinkshere" class="mw-list-item"><a href="/wiki/Especial:LoQueEnlazaAqu%C3%AD/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Lista de todas las páginas de la wiki que enlazan aquí [j]" accesskey="j"><span>Lo que enlaza aquí</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/wiki/Especial:CambiosEnEnlazadas/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" rel="nofollow" title="Cambios recientes en las páginas que enlazan con esta [k]" accesskey="k"><span>Cambios en enlazadas</span></a></li><li id="t-upload" class="mw-list-item"><a href="//commons.wikimedia.org/wiki/Special:UploadWizard?uselang=es" title="Subir archivos [u]" accesskey="u"><span>Subir archivo</span></a></li><li id="t-specialpages" class="mw-list-item"><a href="/wiki/Especial:P%C3%A1ginasEspeciales" title="Lista de todas las páginas especiales [q]" accesskey="q"><span>Páginas especiales</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;oldid=149436018" title="Enlace permanente a esta versión de la página"><span>Enlace permanente</span></a></li><li id="t-info" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=info" title="Más información sobre esta página"><span>Información de la página</span></a></li><li id="t-cite" class="mw-list-item"><a href="/w/index.php?title=Especial:Citar&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;id=149436018&amp;wpFormIdentifier=titleform" title="Información sobre cómo citar esta página"><span>Citar esta página</span></a></li><li id="t-urlshortener" class="mw-list-item"><a href="/w/index.php?title=Especial:Acortador_de_URL&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22"><span>Obtener URL acortado</span></a></li><li id="t-urlshortener-qrcode" class="mw-list-item"><a href="/w/index.php?title=Especial:QrCode&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22"><span>Download QR code</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-coll-print_export" class="vector-menu mw-portlet mw-portlet-coll-print_export"  >
	<div class="vector-menu-heading">
		Imprimir/exportar
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="coll-create_a_book" class="mw-list-item"><a href="/w/index.php?title=Especial:Libro&amp;bookcmd=book_creator&amp;referer=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2021-22"><span>Crear un libro</span></a></li><li id="coll-download-as-rl" class="mw-list-item"><a href="/w/index.php?title=Especial:DownloadAsPdf&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=show-download-screen"><span>Descargar como PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;printable=yes" title="Versión imprimible de esta página [p]" accesskey="p"><span>Versión para imprimir</span></a></li>
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
					
					
					<div id="mw-content-text" class="mw-body-content"><div class="mw-content-ltr mw-parser-output" lang="es" dir="ltr"><div class="noprint AP rellink"><span style="font-size:88%">Artículo principal:</span>&#32;<i><a href="/wiki/Liga_de_Campeones_de_la_UEFA_2021-22" title="Liga de Campeones de la UEFA 2021-22"> Liga de Campeones de la UEFA 2021-22</a></i></div>
<p>En los <b>Octavos de final de la <a href="/wiki/Liga_de_Campeones_de_la_UEFA_2022-23" title="Liga de Campeones de la UEFA 2022-23">Liga de Campeones de la UEFA 2022-23</a></b>, participarán los dieciséis equipos que terminaron primeros y segundos de cada grupo en la fase anterior. Estos fueron distribuidos en ocho parejas. Cada pareja se enfrentará en partidos de ida y vuelta de 90 minutos cada uno. En estos encuentros no se considerará la <a href="/wiki/Regla_del_gol_de_visitante" title="Regla del gol de visitante">regla del gol de visitante</a>. En caso de que no hubiese ganador en el período regular, se realizaría una prórroga de 30 minutos, y si no hay ganador se realizarían <a href="/wiki/Tiros_desde_el_punto_penal" title="Tiros desde el punto penal">tiros desde el punto penal</a>. El sorteo se realizó el 13 de diciembre de 2022 a las 15:00 en <a href="/wiki/Nyon" title="Nyon">Nyon</a>, <a href="/wiki/Suiza" title="Suiza">Suiza</a>.
</p>
<meta property="mw:PageProp/toc" />
<h2><span id="Cuadro_de_clasificaci.C3.B3n"></span><span class="mw-headline" id="Cuadro_de_clasificación">Cuadro de clasificación</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=1" title="Editar sección: Cuadro de clasificación"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="columns" style="-moz-column-count:2; -webkit-column-count:2; column-count:2;">
</div>
<center>
<table cellspacing="0" style="background: #f9f9f9; border: 1px #aaa solid; border-collapse: collapse;" width="60%">

<tbody><tr style="color:black" bgcolor="#ccddcc">
<th>Grupo
</th>
<th>Bombo 1
<p><span style="white-space:nowrap">(Líderes de grupo)</span>
</p>
</th>
<th>Bombo 2
<p><span style="white-space:nowrap">(Segundos de grupo)</span> 
</p>
</th></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2021-22">A</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2021-22">B</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2021-22">C</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Sporting_de_Portugal" class="mw-redirect" title="Sporting de Portugal">Sporting de Portugal</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2021-22">D</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2021-22">E</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2021-22">F</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2021-22">G</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Lille_Olympique_Sporting_Club" title="Lille Olympique Sporting Club">Lille</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Austria.svg" class="mw-file-description" title="Bandera de Austria"><img alt="Bandera de Austria" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/20px-Flag_of_Austria.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/30px-Flag_of_Austria.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/40px-Flag_of_Austria.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Red_Bull_Salzburgo" title="Red Bull Salzburgo">Salzburgo</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2021-22">H</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</td></tr></tbody></table>
</center>
<h2><span class="mw-headline" id="Participantes">Participantes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=2" title="Editar sección: Participantes"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table width="100%">

<tbody><tr align="center">
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/60px-Flag_of_the_Netherlands.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/90px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/120px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</th>
<th><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</th>
<th><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</th>
<th><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</th>
<th><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</th>
<th><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</th>
<th><a href="/wiki/Lille_Olympique_Sporting_Club" title="Lille Olympique Sporting Club">Lille</a>
</th>
<th><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</th></tr>
<tr>
<th>Clasificado
</th>
<th>Clasificado
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
<th>Eliminado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a3/Kit_left_arm_mancity2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3b/Kit_body_mancity2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_right_arm_mancity2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#61ACDF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2122H1.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/bf/Kit_socks_mancity2122H1.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bd/Kit_left_arm_liverpool2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_body_liverpool2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/97/Kit_right_arm_liverpool2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_shorts_liverpool2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DD0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/6b/Kit_socks_liverpool2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ajax2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2a/Kit_left_arm_ajax2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ajax2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_body_ajax2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ajax2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/20/Kit_right_arm_ajax2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ajax1718h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ee/Kit_shorts_ajax1718h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_river1011h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/93/Kit_socks_river1011h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_left_arm_realmadrid2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/22/Kit_body_realmadrid2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/25/Kit_right_arm_realmadrid2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f8/Kit_shorts_realmadrid2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/78/Kit_socks_realmadrid2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c5/Kit_left_arm_bayern2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/db/Kit_body_bayern2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3b/Kit_right_arm_bayern2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c8/Kit_shorts_bayern2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#B51A1E"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbayern2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_socks_fcbayern2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_manutd2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_left_arm_manutd2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_manutd2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_body_manutd2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_manutd2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8a/Kit_right_arm_manutd2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidascondivo20wr.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/18/Kit_shorts_adidascondivo20wr.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_manutd2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b7/Kit_socks_manutd2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_lille2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_left_arm_lille2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_lille2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d9/Kit_body_lille2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_lille2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_right_arm_lille2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000050"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000040"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_lille2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/89/Kit_socks_lille2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/53/Kit_left_arm_juventus2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cd/Kit_body_juventus2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b6/Kit_right_arm_juventus2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidascondivo20wb.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/83/Kit_shorts_adidascondivo20wb.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_socks_juventus2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
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
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/60px-Flag_of_Portugal.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/120px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/60px-Flag_of_Portugal.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/120px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Austria.svg" class="mw-file-description" title="Bandera de Austria"><img alt="Bandera de Austria" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/60px-Flag_of_Austria.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/90px-Flag_of_Austria.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/120px-Flag_of_Austria.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a>
</th>
<th><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</th>
<th><a href="/wiki/Sporting_de_Portugal" class="mw-redirect" title="Sporting de Portugal">Sporting de Portugal</a>
</th>
<th><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</th>
<th><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</th>
<th><a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a>
</th>
<th><a href="/wiki/Red_Bull_Salzburgo" title="Red Bull Salzburgo">Salzburgo</a>
</th>
<th><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</th></tr>
<tr>
<th>Eliminado
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
</th>
<th>Clasificado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e5/Kit_left_arm_psg2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/58/Kit_body_psg2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_right_arm_psg2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/98/Kit_shorts_psg2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0A1254"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_psg2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_socks_psg2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_cadm2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/be/Kit_left_arm_cadm2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_cadm2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/37/Kit_body_cadm2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_cadm2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8c/Kit_right_arm_cadm2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0952FD"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atlmadrid2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_shorts_atlmadrid2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0952FD"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_sporting2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/66/Kit_left_arm_sporting2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_sporting2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6e/Kit_body_sporting2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_sporting2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bd/Kit_right_arm_sporting2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_sporting1718h2.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/9c/Kit_socks_sporting1718h2.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#22346B"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_inter2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a2/Kit_left_arm_inter2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#22346B"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_inter2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_body_inter2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#22346B"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_inter2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b2/Kit_right_arm_inter2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_benfica2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b9/Kit_left_arm_benfica2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_benfica2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/93/Kit_body_benfica2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_benfica2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/73/Kit_right_arm_benfica2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a4/Kit_left_arm_villarreal2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_body_villarreal2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f8/Kit_right_arm_villarreal2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFF00"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_villarreal2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/50/Kit_socks_villarreal2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_nikestrike3w.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_left_arm_nikestrike3w.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rbs2122uh.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/03/Kit_body_rbs2122uh.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_nikestrike3w.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/90/Kit_right_arm_nikestrike3w.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_pol18h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/94/Kit_socks_pol18h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_left_arm_chelsea2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9b/Kit_body_chelsea2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/61/Kit_right_arm_chelsea2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a8/Kit_shorts_chelsea2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/e9/Kit_socks_chelsea2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
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
<h2><span class="mw-headline" id="Estadios">Estadios</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=3" title="Editar sección: Estadios"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span typeof="mw:File"><a href="/wiki/Archivo:Etihad_Stadium_at_night_-_2015.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/200px-Etihad_Stadium_at_night_-_2015.jpg" decoding="async" width="200" height="105" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/300px-Etihad_Stadium_at_night_-_2015.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/400px-Etihad_Stadium_at_night_-_2015.jpg 2x" data-file-width="1024" data-file-height="537" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Panorama_of_Anfield_with_new_main_stand_(29676137824).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/200px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg" decoding="async" width="200" height="136" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/300px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/400px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 2x" data-file-width="3148" data-file-height="2143" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Amsterdam_Arena_Roof_Open.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Amsterdam_Arena_Roof_Open.jpg/200px-Amsterdam_Arena_Roof_Open.jpg" decoding="async" width="200" height="123" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Amsterdam_Arena_Roof_Open.jpg/300px-Amsterdam_Arena_Roof_Open.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Amsterdam_Arena_Roof_Open.jpg/400px-Amsterdam_Arena_Roof_Open.jpg 2x" data-file-width="1374" data-file-height="846" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Estadio_Santiago_Bernabeu.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Estadio_Santiago_Bernabeu.jpg/200px-Estadio_Santiago_Bernabeu.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Estadio_Santiago_Bernabeu.jpg/300px-Estadio_Santiago_Bernabeu.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Estadio_Santiago_Bernabeu.jpg/400px-Estadio_Santiago_Bernabeu.jpg 2x" data-file-width="2816" data-file-height="2112" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a></b><br />
<p>Ciudad: <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a><br />
Capacidad: <b>55 097</b> espectadores<br />
Club:  <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</p>
</td>
<td><b><a href="/wiki/Anfield" title="Anfield">Anfield</a></b><br />
<p>Ciudad:  <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a><br />
Capacidad: <b>54 074</b> espectadores<br />
Club:  <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</p>
</td>
<td><b><a href="/wiki/Johan_Cruyff_Arena" title="Johan Cruyff Arena">Johan Cruyff Arena</a></b><br />
<p>Ciudad:  <a href="/wiki/%C3%81msterdam" title="Ámsterdam">Ámsterdam</a><br />
Capacidad: <b>54 990</b> espectadores<br />
Club:  <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a></b><br />
<p>Ciudad:  <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>81 044</b> espectadores<br />
Club:  <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span typeof="mw:File"><a href="/wiki/Archivo:M%C3%BCnchen_-_Allianz-Arena_(Luftbild).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/200px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/300px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/400px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg 2x" data-file-width="1484" data-file-height="840" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Manchester_United_Panorama_(8051523746).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/Manchester_United_Panorama_%288051523746%29.jpg/200px-Manchester_United_Panorama_%288051523746%29.jpg" decoding="async" width="200" height="96" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/Manchester_United_Panorama_%288051523746%29.jpg/300px-Manchester_United_Panorama_%288051523746%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/33/Manchester_United_Panorama_%288051523746%29.jpg/400px-Manchester_United_Panorama_%288051523746%29.jpg 2x" data-file-width="2500" data-file-height="1197" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg/200px-Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg/300px-Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg/400px-Lille_vs_PSG_2019_-_Stade_Pierre_Mauroy.jpg 2x" data-file-width="4800" data-file-height="3599" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Juventus_v_Real_Madrid,_Champions_League,_Stadium,_Turin,_2013.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg/200px-Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg/300px-Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg/400px-Juventus_v_Real_Madrid%2C_Champions_League%2C_Stadium%2C_Turin%2C_2013.jpg 2x" data-file-width="4608" data-file-height="2592" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a></b><br />
<p>Ciudad:  <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a><br />
Capacidad: <b>75 000</b> espectadores<br />
Club:  <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</p>
</td>
<td><b><a href="/wiki/Old_Trafford" title="Old Trafford">Old Trafford</a></b><br />
<p>Ciudad:  <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a><br />
Capacidad: <b>74 879</b> espectadores<br />
Club:  <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Pierre-Mauroy" title="Estadio Pierre-Mauroy">Stade Pierre-Mauroy</a></b><br />
<p>Ciudad:  <a href="/wiki/Lille" title="Lille">Lille</a><br />
Capacidad: <b>50 186</b> espectadores<br />
Club:  <a href="/wiki/Lille_Olympique_Sporting_Club" title="Lille Olympique Sporting Club">Lille</a>
</p>
</td>
<td><b><a href="/wiki/Juventus_Stadium" title="Juventus Stadium">Juventus Stadium</a></b><br />
<p>Ciudad:  <a href="/wiki/Tur%C3%ADn" title="Turín">Turín</a><br />
Capacidad: <b>41 000</b> espectadores<br />
Club:  <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Estadio_Wanda_Metropolitano_(2018).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/200px-Estadio_Wanda_Metropolitano_%282018%29.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/300px-Estadio_Wanda_Metropolitano_%282018%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/400px-Estadio_Wanda_Metropolitano_%282018%29.jpg 2x" data-file-width="4896" data-file-height="3672" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Jose-Alvalade-Stadion_in_Lissabon.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Jose-Alvalade-Stadion_in_Lissabon.jpg/200px-Jose-Alvalade-Stadion_in_Lissabon.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Jose-Alvalade-Stadion_in_Lissabon.jpg/300px-Jose-Alvalade-Stadion_in_Lissabon.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/59/Jose-Alvalade-Stadion_in_Lissabon.jpg/400px-Jose-Alvalade-Stadion_in_Lissabon.jpg 2x" data-file-width="640" data-file-height="480" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Stadio_Meazza.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Stadio_Meazza.jpg/200px-Stadio_Meazza.jpg" decoding="async" width="200" height="124" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Stadio_Meazza.jpg/300px-Stadio_Meazza.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/11/Stadio_Meazza.jpg/400px-Stadio_Meazza.jpg 2x" data-file-width="3608" data-file-height="2232" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a></b><br />
<p>Ciudad:  <a href="/wiki/Par%C3%ADs" title="París">París</a><br />
Capacidad: <b>48 583</b> espectadores<br />
Club:  <a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Metropolitano_(Madrid)" title="Estadio Metropolitano (Madrid)">Wanda Metropolitano</a></b><br />
<p>Ciudad:  <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>68 456</b> espectadores<br />
Club: <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Jos%C3%A9_Alvalade" title="Estadio José Alvalade">Estadio José Alvalade</a></b><br />
<p>Ciudad:  <a href="/wiki/Lisboa" title="Lisboa">Lisboa</a><br />
Capacidad: <b>50 044</b> espectadores<br />
Club:  <a href="/wiki/Sporting_de_Portugal" class="mw-redirect" title="Sporting de Portugal">Sporting de Portugal</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">Giuseppe Meazza</a></b> <br />
<p>Ciudad:  <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a> <br />
Capacidad: <b>80 018</b> espectadores<br />
Club:  <a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span typeof="mw:File"><a href="/wiki/Archivo:Estadio_da_Luz_-_panoramio_(7).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Estadio_da_Luz_-_panoramio_%287%29.jpg/200px-Estadio_da_Luz_-_panoramio_%287%29.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Estadio_da_Luz_-_panoramio_%287%29.jpg/300px-Estadio_da_Luz_-_panoramio_%287%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/11/Estadio_da_Luz_-_panoramio_%287%29.jpg/400px-Estadio_da_Luz_-_panoramio_%287%29.jpg 2x" data-file-width="3600" data-file-height="2397" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:ESTADIO3.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/ESTADIO3.jpg/200px-ESTADIO3.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/ESTADIO3.jpg/300px-ESTADIO3.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/13/ESTADIO3.jpg/400px-ESTADIO3.jpg 2x" data-file-width="2240" data-file-height="1260" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:EM-Stadion_Wals-Siezenheim_zur_Euro.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f5/EM-Stadion_Wals-Siezenheim_zur_Euro.jpg/200px-EM-Stadion_Wals-Siezenheim_zur_Euro.jpg" decoding="async" width="200" height="94" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f5/EM-Stadion_Wals-Siezenheim_zur_Euro.jpg/300px-EM-Stadion_Wals-Siezenheim_zur_Euro.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f5/EM-Stadion_Wals-Siezenheim_zur_Euro.jpg/400px-EM-Stadion_Wals-Siezenheim_zur_Euro.jpg 2x" data-file-width="2691" data-file-height="1267" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Chelsea_Football_Club,_Stamford_Bridge_11.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg/200px-Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg/300px-Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg/400px-Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg 2x" data-file-width="4608" data-file-height="3456" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Est%C3%A1dio_da_Luz" title="Estádio da Luz">Estádio da Luz</a></b><br />
<p>Ciudad:  <a href="/wiki/Lisboa" title="Lisboa">Lisboa</a><br />
Capacidad: <b>66 500</b> espectadores<br />
Club:  <a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_de_la_Cer%C3%A1mica" title="Estadio de la Cerámica">Estadio de la Cerámica</a></b><br />
<p>Ciudad:  <a href="/wiki/Villarreal" title="Villarreal">Villarreal</a><br />
Capacidad: <b>23 500</b> espectadores<br />
Club:  <a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a>
</p>
</td>
<td><b><a href="/wiki/Red_Bull_Arena_(Salzburgo)" title="Red Bull Arena (Salzburgo)">Red Bull Arena</a></b><br />
<p>Ciudad: <a href="/wiki/Salzburgo" title="Salzburgo">Salzburgo</a><br />
Capacidad: <b>31 895</b> espectadores<br />
Club:  <a href="/wiki/Red_Bull_Salzburgo" title="Red Bull Salzburgo">Salzburgo</a>
</p>
</td>
<td><b><a href="/wiki/Stamford_Bridge_(estadio)" title="Stamford Bridge (estadio)">Stamford Bridge</a></b><br />
<p>Ciudad:  <a href="/wiki/Londres" title="Londres">Londres</a><br />
Capacidad: <b>41 841</b> espectadores<br />
Club:  <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</p>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Llaves">Llaves</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=4" title="Editar sección: Llaves"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
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
<td style="text-align: right;"><a href="/wiki/Red_Bull_Salzburgo" title="Red Bull Salzburgo">Salzburgo</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Austria.svg" class="mw-file-description" title="Bandera de Austria"><img alt="Bandera de Austria" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/20px-Flag_of_Austria.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/30px-Flag_of_Austria.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/40px-Flag_of_Austria.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">2–8
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <b><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#SAL_BAY">1–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BAY_SAL">1–7</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Sporting_de_Portugal" class="mw-redirect" title="Sporting de Portugal">Sporting de Portugal</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td style="text-align: center;">0–5
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#SCP_MCI">0–5</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MCI_SCP">0–0</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td style="text-align: center;">3–2
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BEN_AJA">2–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#AJA_BEN">1–0</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;">4–1
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Lille_Olympique_Sporting_Club" title="Lille Olympique Sporting Club">Lille</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#CHE_LIL">2–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LIL_CHE">2–1</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="text-align: center;">2–1
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#ATM_MUN">1–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MUN_ATM">1–0</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="text-align: center;">4–1
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#VIL_JUV">1–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#JUV_VIL">3–0</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="text-align: center;">1–2
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <b><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#INT_LIV">0–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LIV_INT">1–0</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">2–3
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <b><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#PSG_RMA">1–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#RMA_PSG">1–3</a>
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Enfrentamientos">Enfrentamientos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=5" title="Editar sección: Enfrentamientos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li>Los horarios de los partidos corresponden a la <a href="/wiki/Hora_central_europea" title="Hora central europea">hora central europea</a> (CET <a href="/wiki/UTC%2B01:00" title="UTC+01:00">UTC+1</a>).</li></ul>
<h3><span id="Salzburgo_.E2.80.93_Bayern_M.C3.BAnich"></span><span class="mw-headline" id="Salzburgo_–_Bayern_Múnich">Salzburgo – Bayern Múnich</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=6" title="Editar sección: Salzburgo – Bayern Múnich"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="SAL_BAY">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 16 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Red_Bull_Salzburgo" title="Red Bull Salzburgo">Salzburgo</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Austria.svg" class="mw-file-description" title="Bandera de Austria"><img alt="Bandera de Austria" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/20px-Flag_of_Austria.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/30px-Flag_of_Austria.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/40px-Flag_of_Austria.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:1</b> (1:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Red_Bull_Arena_(Salzburgo)" title="Red Bull Arena (Salzburgo)">Red Bull Arena</a>,</span> <a href="/wiki/Salzburgo" title="Salzburgo">Salzburgo</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Chukwubuike_Adamu" class="mw-redirect" title="Chukwubuike Adamu">Adamu</a> <span typeof="mw:File"><span title="Anotado en el minuto 21"><img alt="Anotado en el minuto 21" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">21'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033896--salzburg-vs-bayern/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 90"><img alt="Anotado en el minuto 90" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">90'</small> <a href="/wiki/Kingsley_Coman" title="Kingsley Coman">Coman</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 29 520 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Michael_Oliver_(%C3%A1rbitro)" title="Michael Oliver (árbitro)">Michael Oliver</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/w/index.php?title=Chris_Kavanagh&amp;action=edit&amp;redlink=1" class="new" title="Chris Kavanagh (aún no redactado)">Chris Kavanagh</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_nikestrike3w.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_left_arm_nikestrike3w.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rbs2122uh.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/03/Kit_body_rbs2122uh.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_nikestrike3w.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/90/Kit_right_arm_nikestrike3w.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_pol18h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/94/Kit_socks_pol18h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c5/Kit_left_arm_bayern2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/db/Kit_body_bayern2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3b/Kit_right_arm_bayern2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c8/Kit_shorts_bayern2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#B51A1E"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbayern2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_socks_fcbayern2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BAY_SAL">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 8 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>7:1 <style data-mw-deduplicate="TemplateStyles:r144106874">.mw-parser-output .sinnegrita,.mw-parser-output .sinnegrita b{font-weight:normal}</style><span class="sinnegrita">(4:0)</span></b> </div><div style="font-size: 85%">(Global <b>8:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Austria.svg" class="mw-file-description" title="Bandera de Austria"><img alt="Bandera de Austria" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/20px-Flag_of_Austria.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/30px-Flag_of_Austria.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/40px-Flag_of_Austria.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Red_Bull_Salzburgo" title="Red Bull Salzburgo">Salzburgo</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a>,</span> <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Robert_Lewandowski" title="Robert Lewandowski">Lewandowski</a> <span typeof="mw:File"><span title="Anotado en los minutos 11, 21&#160;y 23"><img alt="Anotado en los minutos 11, 21&#160;y 23" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">11'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small>,&#160;<small style="vertical-align: middle;">21'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small>,&#160;<small style="vertical-align: middle;">23'</small></li>
<li><a href="/wiki/Serge_Gnabry" title="Serge Gnabry">Gnabry</a> <span typeof="mw:File"><span title="Anotado en el minuto 31"><img alt="Anotado en el minuto 31" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">31'</small></li>
<li><a href="/wiki/Thomas_M%C3%BCller" title="Thomas Müller">Müller</a> <span typeof="mw:File"><span title="Anotado en los minutos 54&#160;y 83"><img alt="Anotado en los minutos 54&#160;y 83" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">54'</small>,&#160;<small style="vertical-align: middle;">83'</small></li>
<li><a href="/wiki/Leroy_San%C3%A9" title="Leroy Sané">Sané</a> <span typeof="mw:File"><span title="Anotado en el minuto 86"><img alt="Anotado en el minuto 86" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">86'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033906--bayern-vs-salzburg/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 70"><img alt="Anotado en el minuto 70" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">70'</small> <a href="/wiki/Maurits_Kjaergaard" title="Maurits Kjaergaard">Kjaergaard</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 25 000 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Cl%C3%A9ment_Turpin" title="Clément Turpin">Clément Turpin</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=J%C3%A9r%C3%B4me_Brisard&amp;action=edit&amp;redlink=1" class="new" title="Jérôme Brisard (aún no redactado)">Jérôme Brisard</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c5/Kit_left_arm_bayern2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/db/Kit_body_bayern2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3b/Kit_right_arm_bayern2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#B51A1E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c8/Kit_shorts_bayern2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#B51A1E"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbayern2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_socks_fcbayern2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_nikestrike3w.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_left_arm_nikestrike3w.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rbs2122uh.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/03/Kit_body_rbs2122uh.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_nikestrike3w.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/90/Kit_right_arm_nikestrike3w.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_pol18h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/94/Kit_socks_pol18h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Sporting_de_Portugal_.E2.80.93_Manchester_City"></span><span class="mw-headline" id="Sporting_de_Portugal_–_Manchester_City">Sporting de Portugal – Manchester City</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=7" title="Editar sección: Sporting de Portugal – Manchester City"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="SCP_MCI">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 15 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Sporting_de_Portugal" class="mw-redirect" title="Sporting de Portugal">Sporting de Portugal</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:5</b> (0:4)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Jos%C3%A9_Alvalade" title="Estadio José Alvalade">Estadio José Alvalade</a>,</span> <a href="/wiki/Lisboa" title="Lisboa">Lisboa</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033897--sporting-cp-vs-man-city/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 9"><img alt="Anotado en el minuto 9" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">9'</small> <a href="/wiki/Riyad_Mahrez" title="Riyad Mahrez">Mahrez</a></li>
<li><span typeof="mw:File"><span title="Anotado en los minutos 17&#160;y 44"><img alt="Anotado en los minutos 17&#160;y 44" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">17'</small>,&#160;<small style="vertical-align: middle;">44'</small> <a href="/wiki/Bernardo_Silva" title="Bernardo Silva">Bernardo Silva</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 32"><img alt="Anotado en el minuto 32" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">32'</small> <a href="/wiki/Phil_Foden" title="Phil Foden">Foden</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 58"><img alt="Anotado en el minuto 58" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">58'</small> <a href="/wiki/Raheem_Sterling" title="Raheem Sterling">Sterling</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 48 129 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Serbia.svg" class="mw-file-description" title="Bandera de Serbia"><img alt="Bandera de Serbia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/20px-Flag_of_Serbia.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/30px-Flag_of_Serbia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/40px-Flag_of_Serbia.svg.png 2x" data-file-width="1350" data-file-height="900" /></a></span></span> <a href="/wiki/Sr%C4%91an_Jovanovi%C4%87" title="Srđan Jovanović">Srđan Jovanović</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Marco_Fritz&amp;action=edit&amp;redlink=1" class="new" title="Marco Fritz (aún no redactado)">Marco Fritz</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_sporting2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/66/Kit_left_arm_sporting2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_sporting2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6e/Kit_body_sporting2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_sporting2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bd/Kit_right_arm_sporting2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_sporting1718h2.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/9c/Kit_socks_sporting1718h2.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_left_arm_mancity2122T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9b/Kit_body_mancity2122T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_right_arm_mancity2122T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#1A2040"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2122T.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_socks_mancity2122T.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MCI_SCP">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 9 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:0</b> </div><div style="font-size: 85%">(Global <b>5:0</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Sporting_de_Portugal" class="mw-redirect" title="Sporting de Portugal">Sporting de Portugal</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a>,</span> <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033907--man-city-vs-sporting-cp/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 51 213 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/w/index.php?title=Halil_Umut_Meler&amp;action=edit&amp;redlink=1" class="new" title="Halil Umut Meler (aún no redactado)">Halil Umut Meler</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/w/index.php?title=Paolo_Valeri&amp;action=edit&amp;redlink=1" class="new" title="Paolo Valeri (aún no redactado)">Paolo Valeri</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a3/Kit_left_arm_mancity2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3b/Kit_body_mancity2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_right_arm_mancity2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#61ACDF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#61ACDF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2122H1.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/bf/Kit_socks_mancity2122H1.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_sporting2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/90/Kit_left_arm_sporting2122t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_sporting2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cb/Kit_body_sporting2122t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_sporting2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/36/Kit_right_arm_sporting2122t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Benfica_.E2.80.93_Ajax"></span><span class="mw-headline" id="Benfica_–_Ajax">Benfica – Ajax</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=8" title="Editar sección: Benfica – Ajax"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BEN_AJA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 23 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:2</b> (1:2)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Est%C3%A1dio_da_Luz" title="Estádio da Luz">Estádio da Luz</a>,</span> <a href="/wiki/Lisboa" title="Lisboa">Lisboa</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/S%C3%A9bastien_Haller" title="Sébastien Haller">Haller</a> <span typeof="mw:File"><span title="Anotado en el minuto 26"><img alt="Anotado en el minuto 26" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">26'&#160;(<a href="/wiki/Autogol" title="Autogol">a.g.</a>)</small></li>
<li><a href="/wiki/Roman_Yaremchuk" title="Roman Yaremchuk">Yaremchuk</a> <span typeof="mw:File"><span title="Anotado en el minuto 72"><img alt="Anotado en el minuto 72" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">72'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033900--benfica-vs-ajax/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 18"><img alt="Anotado en el minuto 18" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">18'</small> <a href="/wiki/Du%C5%A1an_Tadi%C4%87" title="Dušan Tadić">Tadić</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 29"><img alt="Anotado en el minuto 29" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">29'</small> <a href="/wiki/S%C3%A9bastien_Haller" title="Sébastien Haller">Haller</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 54 760 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Slovenia.svg" class="mw-file-description" title="Bandera de Eslovenia"><img alt="Bandera de Eslovenia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/20px-Flag_of_Slovenia.svg.png" decoding="async" width="20" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/30px-Flag_of_Slovenia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/40px-Flag_of_Slovenia.svg.png 2x" data-file-width="1200" data-file-height="600" /></a></span></span> <a href="/wiki/Slavko_Vin%C4%8Di%C4%87" title="Slavko Vinčić">Slavko Vinčić</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Marco_Fritz&amp;action=edit&amp;redlink=1" class="new" title="Marco Fritz (aún no redactado)">Marco Fritz</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_benfica2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b9/Kit_left_arm_benfica2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_benfica2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/93/Kit_body_benfica2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_benfica2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/73/Kit_right_arm_benfica2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ajax2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/25/Kit_left_arm_ajax2122T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ajax2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/07/Kit_body_ajax2122T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ajax2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_right_arm_ajax2122T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ajax2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/74/Kit_shorts_ajax2122T.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_ajax2122T.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ea/Kit_socks_ajax2122T.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="AJA_BEN">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 15 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div><div style="font-size: 85%">(Global <b>2:3</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Johan_Cruyff_Arena" title="Johan Cruyff Arena">Johan Cruyff Arena</a>,</span> <a href="/wiki/%C3%81msterdam" title="Ámsterdam">Ámsterdam</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033910--ajax-vs-benfica/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 77"><img alt="Anotado en el minuto 77" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">77'</small> <a href="/wiki/Darwin_N%C3%BA%C3%B1ez" title="Darwin Núñez">Núñez</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 54 066 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Carlos_del_Cerro_Grande" title="Carlos del Cerro Grande">Del Cerro Grande</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ajax2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2a/Kit_left_arm_ajax2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ajax2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_body_ajax2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ajax2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/20/Kit_right_arm_ajax2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ajax1718h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ee/Kit_shorts_ajax1718h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_river1011h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/9/93/Kit_socks_river1011h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_benfica2021a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7d/Kit_body_benfica2021a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_benfica2021a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/66/Kit_shorts_benfica2021a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Chelsea_.E2.80.93_Lille"></span><span class="mw-headline" id="Chelsea_–_Lille">Chelsea – Lille</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=9" title="Editar sección: Chelsea – Lille"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="CHE_LIL">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 22 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:0</b> (1:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Lille_Olympique_Sporting_Club" title="Lille Olympique Sporting Club">Lille</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Stamford_Bridge_(estadio)" title="Stamford Bridge (estadio)">Stamford Bridge</a>,</span> <a href="/wiki/Londres" title="Londres">Londres</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Kai_Havertz" title="Kai Havertz">Havertz</a> <span typeof="mw:File"><span title="Anotado en el minuto 8"><img alt="Anotado en el minuto 8" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">8'</small></li>
<li><a href="/wiki/Christian_Pulisic" title="Christian Pulisic">Pulisic</a> <span typeof="mw:File"><span title="Anotado en el minuto 63"><img alt="Anotado en el minuto 63" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">63'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033901--chelsea-vs-losc/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 38 832 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Jes%C3%BAs_Gil_Manzano" title="Jesús Gil Manzano">Gil Manzano</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_left_arm_chelsea2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9b/Kit_body_chelsea2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/61/Kit_right_arm_chelsea2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_chelsea2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a8/Kit_shorts_chelsea2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/e9/Kit_socks_chelsea2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_lille2122a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a9/Kit_left_arm_lille2122a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_lille2122a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0e/Kit_body_lille2122a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_lille2122a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/da/Kit_right_arm_lille2122a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_lille2122a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/81/Kit_shorts_lille2122a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_crc2122a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/c3/Kit_socks_crc2122a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LIL_CHE">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 16 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Lille_Olympique_Sporting_Club" title="Lille Olympique Sporting Club">Lille</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:2 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:1)</span></b> </div><div style="font-size: 85%">(Global <b>1:4</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Pierre-Mauroy" title="Estadio Pierre-Mauroy">Stade Pierre-Mauroy</a>,</span> <a href="/wiki/Lille" title="Lille">Lille</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Burak_Y%C4%B1lmaz" title="Burak Yılmaz">Yılmaz</a> <span typeof="mw:File"><span title="Anotado en el minuto 38"><img alt="Anotado en el minuto 38" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">38'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033911--losc-vs-chelsea/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 45+3"><img alt="Anotado en el minuto 45+3" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">45+3'</small> <a href="/wiki/Christian_Pulisic" title="Christian Pulisic">Pulisic</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 71"><img alt="Anotado en el minuto 71" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">71'</small> <a href="/wiki/C%C3%A9sar_Azpilicueta" title="César Azpilicueta">Azpilicueta</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 49 048 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Davide_Massa" title="Davide Massa">Davide Massa</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_lille2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_left_arm_lille2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_lille2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d9/Kit_body_lille2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_lille2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_right_arm_lille2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000050"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000050"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_lille2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/89/Kit_socks_lille2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2122A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7a/Kit_left_arm_chelsea2122A.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2122A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_body_chelsea2122A.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2122A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e9/Kit_right_arm_chelsea2122A.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFF242"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea2122A.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/c8/Kit_socks_chelsea2122A.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Atl.C3.A9tico_de_Madrid_.E2.80.93_Manchester_United"></span><span class="mw-headline" id="Atlético_de_Madrid_–_Manchester_United">Atlético de Madrid – Manchester United</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=10" title="Editar sección: Atlético de Madrid – Manchester United"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="ATM_MUN">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 23 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:1</b> (1:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Metropolitano_(Madrid)" title="Estadio Metropolitano (Madrid)">Estadio Metropolitano</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Jo%C3%A3o_F%C3%A9lix" title="João Félix">João Félix</a> <span typeof="mw:File"><span title="Anotado en el minuto 7"><img alt="Anotado en el minuto 7" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">7'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033902--atletico-vs-man-united/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 80"><img alt="Anotado en el minuto 80" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">80'</small> <a href="/wiki/Anthony_Elanga" title="Anthony Elanga">Elanga</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 63 273 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Romania.svg" class="mw-file-description" title="Bandera de Rumania"><img alt="Bandera de Rumania" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/20px-Flag_of_Romania.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/30px-Flag_of_Romania.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/40px-Flag_of_Romania.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Ovidiu_Ha%C5%A3egan" title="Ovidiu Haţegan">Ovidiu Haţegan</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3a/Kit_left_arm_atlmadrid2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7b/Kit_body_atlmadrid2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/be/Kit_right_arm_atlmadrid2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atlmadrid2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_shorts_atlmadrid2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_manutd2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b4/Kit_left_arm_manutd2122t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_manutd2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7d/Kit_body_manutd2122t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_manutd2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/ca/Kit_right_arm_manutd2122t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_manutd2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a3/Kit_shorts_manutd2122t.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_manutd2122t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/f4/Kit_socks_manutd2122t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MUN_ATM">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 15 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:1)</span></b> </div><div style="font-size: 85%">(Global <b>1:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Old_Trafford" title="Old Trafford">Old Trafford</a>,</span> <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033908--man-united-vs-atletico/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 41"><img alt="Anotado en el minuto 41" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">41'</small> <a href="/wiki/Renan_Lodi" title="Renan Lodi">Renan Lodi</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 73 008 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Slovenia.svg" class="mw-file-description" title="Bandera de Eslovenia"><img alt="Bandera de Eslovenia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/20px-Flag_of_Slovenia.svg.png" decoding="async" width="20" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/30px-Flag_of_Slovenia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/40px-Flag_of_Slovenia.svg.png 2x" data-file-width="1200" data-file-height="600" /></a></span></span> <a href="/wiki/Slavko_Vin%C4%8Di%C4%87" title="Slavko Vinčić">Slavko Vinčić</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Marco_Fritz&amp;action=edit&amp;redlink=1" class="new" title="Marco Fritz (aún no redactado)">Marco Fritz</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_manutd2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_left_arm_manutd2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_manutd2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_body_manutd2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_manutd2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8a/Kit_right_arm_manutd2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidascondivo20wr.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/18/Kit_shorts_adidascondivo20wr.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_manutd2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b7/Kit_socks_manutd2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#2D70B7"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_left_arm_atlmadrid2122t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#2D70B7"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6e/Kit_body_atlmadrid2122t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#2D70B7"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5a/Kit_right_arm_atlmadrid2122t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#2D70B7"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atlmadrid2122t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/02/Kit_shorts_atlmadrid2122t.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#2D70B7"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atlmadrid2122t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/49/Kit_socks_atlmadrid2122t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Villarreal_.E2.80.93_Juventus"></span><span class="mw-headline" id="Villarreal_–_Juventus">Villarreal – Juventus</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=11" title="Editar sección: Villarreal – Juventus"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="VIL_JUV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 22 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:1</b> (0:1)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_de_la_Cer%C3%A1mica" title="Estadio de la Cerámica">Estadio de la Cerámica</a>,</span> <a href="/wiki/Villarreal" title="Villarreal">Villarreal</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Dani_Parejo" title="Dani Parejo">Parejo</a> <span typeof="mw:File"><span title="Anotado en el minuto 66"><img alt="Anotado en el minuto 66" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">66'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033903--villarreal-vs-juventus/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 1"><img alt="Anotado en el minuto 1" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">1'</small> <a href="/wiki/Du%C5%A1an_Vlahovi%C4%87" title="Dušan Vlahović">Vlahović</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 17 686 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Daniel_Siebert" title="Daniel Siebert">Daniel Siebert</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bastian_Dankert" title="Bastian Dankert">Bastian Dankert</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a4/Kit_left_arm_villarreal2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_body_villarreal2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f8/Kit_right_arm_villarreal2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFF00"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_villarreal2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/50/Kit_socks_villarreal2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/53/Kit_left_arm_juventus2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cd/Kit_body_juventus2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b6/Kit_right_arm_juventus2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidascondivo20wb.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/83/Kit_shorts_adidascondivo20wb.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_socks_juventus2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="JUV_VIL">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 16 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:3 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div><div style="font-size: 85%">(Global <b>1:4</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Juventus_Stadium" title="Juventus Stadium">Juventus Stadium</a>,</span> <a href="/wiki/Tur%C3%ADn" title="Turín">Turín</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033909--juventus-vs-villarreal/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 78"><img alt="Anotado en el minuto 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">78'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small> <a href="/wiki/Gerard_Moreno" title="Gerard Moreno">Moreno</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 85"><img alt="Anotado en el minuto 85" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">85'</small> <a href="/wiki/Pau_Torres" title="Pau Torres">Torres</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 90+2"><img alt="Anotado en el minuto 90+2" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">90+2'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small> <a href="/wiki/Arnaut_Danjuma" title="Arnaut Danjuma">Danjuma</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 30 385 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/w/index.php?title=Tomasz_Kwiatkowski&amp;action=edit&amp;redlink=1" class="new" title="Tomasz Kwiatkowski (aún no redactado)">Tomasz Kwiatkowski</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/53/Kit_left_arm_juventus2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cd/Kit_body_juventus2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_juventus2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b6/Kit_right_arm_juventus2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidascondivo20wb.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/83/Kit_shorts_adidascondivo20wb.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/71/Kit_socks_juventus2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a4/Kit_left_arm_villarreal2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_body_villarreal2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_villarreal2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f8/Kit_right_arm_villarreal2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFF00"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_villarreal2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/50/Kit_socks_villarreal2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Inter_de_Mil.C3.A1n_.E2.80.93_Liverpool"></span><span class="mw-headline" id="Inter_de_Milán_–_Liverpool">Inter de Milán – Liverpool</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=12" title="Editar sección: Inter de Milán – Liverpool"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="INT_LIV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 16 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:2</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">Giuseppe Meazza</a>,</span> <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033898--inter-vs-liverpool/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 75"><img alt="Anotado en el minuto 75" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">75'</small> <a href="/wiki/Roberto_Firmino" title="Roberto Firmino">Firmino</a></li>
<li><span typeof="mw:File"><span title="Anotado en el minuto 83"><img alt="Anotado en el minuto 83" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">83'</small> <a href="/wiki/Mohamed_Salah" title="Mohamed Salah">Salah</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 37 918 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/w/index.php?title=Tomasz_Kwiatkowski&amp;action=edit&amp;redlink=1" class="new" title="Tomasz Kwiatkowski (aún no redactado)">Tomasz Kwiatkowski</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#22346B"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_inter2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a2/Kit_left_arm_inter2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#22346B"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_inter2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_body_inter2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#22346B"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_inter2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b2/Kit_right_arm_inter2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bd/Kit_left_arm_liverpool2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_body_liverpool2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/97/Kit_right_arm_liverpool2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_shorts_liverpool2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DD0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/6b/Kit_socks_liverpool2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LIV_INT">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 8 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div><div style="font-size: 85%">(Global <b>2:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Anfield" title="Anfield">Anfield</a>,</span> <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033904--liverpool-vs-inter/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 62"><img alt="Anotado en el minuto 62" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">62'</small> <a href="/wiki/Lautaro_Mart%C3%ADnez" title="Lautaro Martínez">Martínez</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 51 747 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Antonio_Mateu_Lahoz" title="Antonio Mateu Lahoz">Mateu Lahoz</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Juan_Mart%C3%ADnez_Munuera" title="Juan Martínez Munuera">Martínez Munuera</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bd/Kit_left_arm_liverpool2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_body_liverpool2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/97/Kit_right_arm_liverpool2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_liverpool2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_shorts_liverpool2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DD0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/6b/Kit_socks_liverpool2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_inter2122T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_inter2122T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Par.C3.ADs_Saint-Germain_.E2.80.93_Real_Madrid"></span><span class="mw-headline" id="París_Saint-Germain_–_Real_Madrid">París Saint-Germain – Real Madrid</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=13" title="Editar sección: París Saint-Germain – Real Madrid"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="PSG_RMA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 15 de febrero de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a>,</span> <a href="/wiki/Par%C3%ADs" title="París">París</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Kylian_Mbapp%C3%A9" title="Kylian Mbappé">Mbappé</a> <span typeof="mw:File"><span title="Anotado en el minuto 90+4"><img alt="Anotado en el minuto 90+4" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">90+4'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033899--paris-vs-real-madrid/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 47 443 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Daniele_Orsato" title="Daniele Orsato">Daniele Orsato</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/w/index.php?title=Marco_Di_Bello&amp;action=edit&amp;redlink=1" class="new" title="Marco Di Bello (aún no redactado)">Marco Di Bello</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e5/Kit_left_arm_psg2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/58/Kit_body_psg2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_right_arm_psg2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/98/Kit_shorts_psg2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0A1254"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_psg2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_socks_psg2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_left_arm_realmadrid2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/22/Kit_body_realmadrid2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/25/Kit_right_arm_realmadrid2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f8/Kit_shorts_realmadrid2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/78/Kit_socks_realmadrid2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="RMA_PSG">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 9 de marzo de 2022
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:1)</span></b> </div><div style="font-size: 85%">(Global <b>3:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Karim_Benzema" title="Karim Benzema">Benzema</a> <span typeof="mw:File"><span title="Anotado en los minutos 61, 76&#160;y 78"><img alt="Anotado en los minutos 61, 76&#160;y 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">61'</small>,&#160;<small style="vertical-align: middle;">76'</small>,&#160;<small style="vertical-align: middle;">78'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2033905--real-madrid-vs-paris/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><span typeof="mw:File"><span title="Anotado en el minuto 39"><img alt="Anotado en el minuto 39" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">39'</small> <a href="/wiki/Kylian_Mbapp%C3%A9" title="Kylian Mbappé">Mbappé</a></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 59 895 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Pol_van_Boekel" title="Pol van Boekel">Pol van Boekel</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_left_arm_realmadrid2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/22/Kit_body_realmadrid2122H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/25/Kit_right_arm_realmadrid2122H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid2122H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f8/Kit_shorts_realmadrid2122H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid2122H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/78/Kit_socks_realmadrid2122H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e5/Kit_left_arm_psg2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/58/Kit_body_psg2122h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_right_arm_psg2122h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_psg2122h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/98/Kit_shorts_psg2122h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0A1254"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_psg2122h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_socks_psg2122h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Clasificados_para_Cuartos_de_final">Clasificados para Cuartos de final</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=14" title="Editar sección: Clasificados para Cuartos de final"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table align="center" cellpadding="2" cellspacing="0" style="background: #f5faff; border: 1px #aaa solid; border-collapse: collapse; font-size: 95%;" width="80%">

<tbody><tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/45px-Flag_of_Germany.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/68px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/45px-Flag_of_Portugal.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/68px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a></b>
</td></tr>
<tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Villarreal_Club_de_F%C3%BAtbol" title="Villarreal Club de Fútbol">Villarreal</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a></b>
</td></tr></tbody></table>
<h2><span id="V.C3.A9ase_tambi.C3.A9n"></span><span class="mw-headline" id="Véase_también">Véase también</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=15" title="Editar sección: Véase también"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/Anexo:Ronda_preliminar_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Ronda preliminar de la Liga de Campeones de la UEFA 2021-22">Anexo: Ronda preliminar de la Liga de Campeones de la UEFA 2021-22</a></li>
<li><a href="/wiki/Anexo:Primera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Primera ronda previa de la Liga de Campeones de la UEFA 2021-22">Anexo: Primera ronda previa de la Liga de Campeones de la UEFA 2021-22</a></li>
<li><a href="/wiki/Anexo:Segunda_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Segunda ronda previa de la Liga de Campeones de la UEFA 2021-22">Anexo: Segunda ronda previa de la Liga de Campeones de la UEFA 2021-22</a></li>
<li><a href="/wiki/Anexo:Tercera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Tercera ronda previa de la Liga de Campeones de la UEFA 2021-22">Anexo: Tercera ronda previa de la Liga de Campeones de la UEFA 2021-22</a></li>
<li><a href="/wiki/Anexo:Cuarta_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Cuarta ronda previa de la Liga de Campeones de la UEFA 2021-22">Anexo: Cuarta ronda previa de la Liga de Campeones de la UEFA 2021-22</a></li>
<li>Fase de grupos <small>(<a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2021-22">Grupo A</a>, <a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2021-22">Grupo B</a>, <a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2021-22">Grupo C</a>, <a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2021-22">Grupo D</a>, <a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2021-22">Grupo E</a>, <a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2021-22">Grupo F</a>, <a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2021-22">Grupo G</a>, <a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2021-22">Grupo H</a>)</small></li>
<li><a href="/wiki/Anexo:Cuartos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Cuartos de final de la Liga de Campeones de la UEFA 2021-22">Anexo: Cuartos de final de la Liga de Campeones de la UEFA 2021-22</a></li>
<li><a href="/wiki/Anexo:Semifinales_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Semifinales de la Liga de Campeones de la UEFA 2021-22">Anexo: Semifinales de la Liga de Campeones de la UEFA 2021-22</a></li>
<li><a href="/wiki/Final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Final de la Liga de Campeones de la UEFA 2021-22">Final de la Liga de Campeones de la UEFA 2021-22</a></li></ul>
<h2><span class="mw-headline" id="Referencias">Referencias</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=16" title="Editar sección: Referencias"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="listaref" style="list-style-type: decimal;"></div>
<h2><span class="mw-headline" id="Enlaces_externos">Enlaces externos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;action=edit&amp;section=17" title="Editar sección: Enlaces externos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://es.uefa.com">Página oficial de la UEFA</a></li>
<li><a rel="nofollow" class="external text" href="http://es.uefa.com/uefachampionsleague/index.html">Página oficial de la UEFA Champions League</a></li></ul>
<p><br clear="all" />
</p>
<table class="wikitable" border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; margin:0 auto;">

<tbody><tr style="text-align: center;">
<td width="30%">Predecesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2020-21" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2020-21">2020-21</a></b>
</td>
<td width="40%"><b>Octavos de final de la<br /><a href="/wiki/Liga_de_Campeones_de_la_UEFA" title="Liga de Campeones de la UEFA">Liga de Campeones de la UEFA</a></b><br />2021-22
</td>
<td width="30%">Sucesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2022-23">2022-23</a></b>
</td></tr></tbody></table>
<!-- 
NewPP limit report
Parsed by mw‐api‐int.codfw.main‐774c7d5bcb‐kbstm
Cached time: 20240212175257
Cache expiry: 2592000
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.741 seconds
Real time usage: 0.885 seconds
Preprocessor visited node count: 24261/1000000
Post‐expand include size: 237906/2097152 bytes
Template argument size: 81376/2097152 bytes
Highest expansion depth: 14/100
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 1318/5000000 bytes
Lua time usage: 0.051/10.000 seconds
Lua memory usage: 1863256/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  380.349      1 -total
 65.06%  247.457     16 Plantilla:Partidos
 20.31%   77.245     80 Plantilla:Bandera
 18.32%   69.673     64 Plantilla:En_varias_líneas
  9.70%   36.879     32 Plantilla:Árbitro
  8.76%   33.303     16 Plantilla:Str_sub
  8.47%   32.229     32 Plantilla:Trim
  8.25%   31.370    120 Plantilla:Bandera_icono
  8.06%   30.653     32 Plantilla:Football_kit
  6.34%   24.097     35 Plantilla:Gol
-->

<!-- Saved in parser cache with key eswiki:pcache:idhash:9710387-0!canonical and timestamp 20240212175256 and revision id 149436018. Rendering was triggered because: api-parse
 -->
</div><!--esi <esi:include src="/esitest-fa8a495983347898/content" /> --><noscript><img src="https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" width="1" height="1" style="border: none; position: absolute;"></noscript>
<div class="printfooter" data-nosnippet="">Obtenido de «<a dir="ltr" href="https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;oldid=149436018">https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;oldid=149436018</a>»</div></div>
					<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Especial:Categor%C3%ADas" title="Especial:Categorías">Categoría</a>: <ul><li><a href="/wiki/Categor%C3%ADa:Liga_de_Campeones_de_la_UEFA_2021-22" title="Categoría:Liga de Campeones de la UEFA 2021-22">Liga de Campeones de la UEFA 2021-22</a></li></ul></div></div>
				</div>
			</main>
			
		</div>
		<div class="mw-footer-container">
			
<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info">
	<li id="footer-info-lastmod"> Esta página se editó por última vez el 22 feb 2023 a las 01:17.</li>
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
	<li id="footer-places-mobileview"><a href="//es.m.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Versión para móviles</a></li>
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
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgHostname":"mw1409","wgBackendResponseTime":137,"wgPageParseReport":{"limitreport":{"cputime":"0.741","walltime":"0.885","ppvisitednodes":{"value":24261,"limit":1000000},"postexpandincludesize":{"value":237906,"limit":2097152},"templateargumentsize":{"value":81376,"limit":2097152},"expansiondepth":{"value":14,"limit":100},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":1318,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  380.349      1 -total"," 65.06%  247.457     16 Plantilla:Partidos"," 20.31%   77.245     80 Plantilla:Bandera"," 18.32%   69.673     64 Plantilla:En_varias_líneas","  9.70%   36.879     32 Plantilla:Árbitro","  8.76%   33.303     16 Plantilla:Str_sub","  8.47%   32.229     32 Plantilla:Trim","  8.25%   31.370    120 Plantilla:Bandera_icono","  8.06%   30.653     32 Plantilla:Football_kit","  6.34%   24.097     35 Plantilla:Gol"]},"scribunto":{"limitreport-timeusage":{"value":"0.051","limit":"10.000"},"limitreport-memusage":{"value":1863256,"limit":52428800}},"cachereport":{"origin":"mw-api-int.codfw.main-774c7d5bcb-kbstm","timestamp":"20240212175257","ttl":2592000,"transientcontent":false}}});});</script>
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
		row_data.append('21/22')
			
		tabla_data.append(row_data)

	#Especicificar nombre del csv donde guardar la tabla
	file_name = 'octavos.csv'
	with open(file_name, 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(tabla_data)
	print(f'Se guardó la tabla en {file_name}')

else:
	print('No se encontró la tabla')