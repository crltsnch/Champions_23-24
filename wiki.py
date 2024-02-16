# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import csv

#Obtener tabla de partidos de octavos del contenido de wikipedia

html = """<!DOCTYPE html>
<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available" lang="es" dir="ltr">
<head>
<meta charset="UTF-8">
<title>Anexo:Octavos de final de la Liga de Campeones de la UEFA 2018-19 - Wikipedia, la enciclopedia libre</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available";var cookie=document.cookie.match(/(?:^|; )eswikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":[",\t."," \t,"],
"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],"wgRequestId":"90505a20-8737-43c6-9c06-80ce0bc8181c","wgCanonicalNamespace":"Anexo","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":104,"wgPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19","wgTitle":"Octavos de final de la Liga de Campeones de la UEFA 2018-19","wgCurRevisionId":154931376,"wgRevisionId":154931376,"wgArticleId":8742721,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Liga de Campeones de la UEFA 2018-19"],"wgPageViewLanguage":"es","wgPageContentLanguage":"es","wgPageContentModel":"wikitext","wgRelevantPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19","wgRelevantArticleId":8742721,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,
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
<meta property="og:title" content="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2018-19 - Wikipedia, la enciclopedia libre">
<meta property="og:type" content="website">
<link rel="preconnect" href="//upload.wikimedia.org">
<link rel="alternate" media="only screen and (max-width: 720px)" href="//es.m.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19">
<link rel="alternate" type="application/x-wiki" title="Editar" href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">
<link rel="icon" href="/static/favicon/wikipedia.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (es)">
<link rel="EditURI" type="application/rsd+xml" href="//es.wikipedia.org/w/api.php?action=rsd">
<link rel="canonical" href="https://es.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">
<link rel="alternate" type="application/atom+xml" title="Canal Atom de Wikipedia" href="/w/index.php?title=Especial:CambiosRecientes&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="//login.wikimedia.org">
</head>
<body class="skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-104 ns-subject mw-editable page-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19 rootpage-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19 skin-vector-2022 action-view"><a class="mw-jump-link" href="#bodyContent">Ir al contenido</a>
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
			<li id="pt-createaccount-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2018-19" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio" class=""><span>Crear una cuenta</span></a>
</li>
<li id="pt-login-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2018-19" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o" class=""><span>Acceder</span></a>
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
			
			<li id="pt-createaccount" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2018-19" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio"><span class="vector-icon mw-ui-icon-userAdd mw-ui-icon-wikimedia-userAdd"></span> <span>Crear una cuenta</span></a></li><li id="pt-login" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2018-19" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o"><span class="vector-icon mw-ui-icon-logIn mw-ui-icon-wikimedia-logIn"></span> <span>Acceder</span></a></li>
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
			<li id="toc-Schalke_04_–_Manchester_City"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Schalke_04_–_Manchester_City">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.1</span>Schalke 04 – Manchester City</div>
			</a>
			
			<ul id="toc-Schalke_04_–_Manchester_City-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Atlético_de_Madrid_–_Juventus"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Atlético_de_Madrid_–_Juventus">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.2</span>Atlético de Madrid – Juventus</div>
			</a>
			
			<ul id="toc-Atlético_de_Madrid_–_Juventus-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Manchester_United_–_París_Saint-Germain"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Manchester_United_–_París_Saint-Germain">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.3</span>Manchester United – París Saint-Germain</div>
			</a>
			
			<ul id="toc-Manchester_United_–_París_Saint-Germain-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Tottenham_Hotspur_–_Borussia_Dortmund"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Tottenham_Hotspur_–_Borussia_Dortmund">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.4</span>Tottenham Hotspur – Borussia Dortmund</div>
			</a>
			
			<ul id="toc-Tottenham_Hotspur_–_Borussia_Dortmund-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Olympique_de_Lyon_–_Barcelona"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Olympique_de_Lyon_–_Barcelona">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.5</span>Olympique de Lyon – Barcelona</div>
			</a>
			
			<ul id="toc-Olympique_de_Lyon_–_Barcelona-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Roma_–_Porto"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Roma_–_Porto">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.6</span>Roma – Porto</div>
			</a>
			
			<ul id="toc-Roma_–_Porto-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Ajax_–_Real_Madrid"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Ajax_–_Real_Madrid">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.7</span>Ajax – Real Madrid</div>
			</a>
			
			<ul id="toc-Ajax_–_Real_Madrid-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Liverpool_–_Bayern_Múnich"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Liverpool_–_Bayern_Múnich">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.8</span>Liverpool – Bayern Múnich</div>
			</a>
			
			<ul id="toc-Liverpool_–_Bayern_Múnich-sublist" class="vector-toc-list">
			</ul>
		</li>
	</ul>
	</li>
	<li id="toc-Clasificados_para_Cuartos_de_Final"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Clasificados_para_Cuartos_de_Final">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">6</span>Clasificados para Cuartos de Final</div>
		</a>
		
		<ul id="toc-Clasificados_para_Cuartos_de_Final-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Referencias"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Referencias">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">7</span>Referencias</div>
		</a>
		
		<ul id="toc-Referencias-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Véase_también"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Véase_también">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">8</span>Véase también</div>
		</a>
		
		<ul id="toc-Véase_también-sublist" class="vector-toc-list">
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
					<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-namespace">Anexo</span><span class="mw-page-title-separator">:</span><span class="mw-page-title-main">Octavos de final de la Liga de Campeones de la UEFA 2018-19</span></h1>
							
<div id="p-lang-btn" class="vector-dropdown mw-portlet mw-portlet-lang"  >
	<input type="checkbox" id="p-lang-btn-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-lang-btn" class="vector-dropdown-checkbox mw-interlanguage-selector" aria-label="Este artículo existe sólo en este idioma. Añade el artículo para otros idiomas"   >
	<label id="p-lang-btn-label" for="p-lang-btn-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--action-progressive mw-portlet-lang-heading-0" aria-hidden="true"  ><span class="vector-icon mw-ui-icon-language-progressive mw-ui-icon-wikimedia-language-progressive"></span>

<span class="vector-dropdown-label-text">Añadir idiomas</span>
	</label>
	<div class="vector-dropdown-content">

		<div class="vector-menu-content">
			
			<ul class="vector-menu-content-list">
				
				
			</ul>
			<div class="after-portlet after-portlet-lang"><span class="uls-after-portlet-link"></span><span class="wb-langlinks-add wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:NewItem?site=eswiki&amp;page=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2018-19" title="Agregar enlaces interlingüísticos" class="wbc-editpage">Añadir enlaces</a></span></div>
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
			
			<li id="ca-nstab-anexo" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Ver la página de contenido [c]" accesskey="c"><span>Anexo</span></a></li><li id="ca-talk" class="new vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo_discusi%C3%B3n:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;redlink=1" rel="discussion" title="Discusión acerca de la página (aún no redactado) [t]" accesskey="t"><span>Discusión</span></a></li>
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
			
			<li id="ca-view" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19"><span>Leer</span></a></li><li id="ca-edit" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-history" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=history" title="Versiones anteriores de esta página [h]" accesskey="h"><span>Ver historial</span></a></li>
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
			
			<li id="ca-more-view" class="selected vector-more-collapsible-item mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19"><span>Leer</span></a></li><li id="ca-more-edit" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-more-history" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=history"><span>Ver historial</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-tb" class="vector-menu mw-portlet mw-portlet-tb"  >
	<div class="vector-menu-heading">
		General
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-whatlinkshere" class="mw-list-item"><a href="/wiki/Especial:LoQueEnlazaAqu%C3%AD/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Lista de todas las páginas de la wiki que enlazan aquí [j]" accesskey="j"><span>Lo que enlaza aquí</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/wiki/Especial:CambiosEnEnlazadas/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" rel="nofollow" title="Cambios recientes en las páginas que enlazan con esta [k]" accesskey="k"><span>Cambios en enlazadas</span></a></li><li id="t-upload" class="mw-list-item"><a href="//commons.wikimedia.org/wiki/Special:UploadWizard?uselang=es" title="Subir archivos [u]" accesskey="u"><span>Subir archivo</span></a></li><li id="t-specialpages" class="mw-list-item"><a href="/wiki/Especial:P%C3%A1ginasEspeciales" title="Lista de todas las páginas especiales [q]" accesskey="q"><span>Páginas especiales</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;oldid=154931376" title="Enlace permanente a esta versión de la página"><span>Enlace permanente</span></a></li><li id="t-info" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=info" title="Más información sobre esta página"><span>Información de la página</span></a></li><li id="t-cite" class="mw-list-item"><a href="/w/index.php?title=Especial:Citar&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;id=154931376&amp;wpFormIdentifier=titleform" title="Información sobre cómo citar esta página"><span>Citar esta página</span></a></li><li id="t-urlshortener" class="mw-list-item"><a href="/w/index.php?title=Especial:Acortador_de_URL&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19"><span>Obtener URL acortado</span></a></li><li id="t-urlshortener-qrcode" class="mw-list-item"><a href="/w/index.php?title=Especial:QrCode&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19"><span>Download QR code</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-coll-print_export" class="vector-menu mw-portlet mw-portlet-coll-print_export"  >
	<div class="vector-menu-heading">
		Imprimir/exportar
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="coll-create_a_book" class="mw-list-item"><a href="/w/index.php?title=Especial:Libro&amp;bookcmd=book_creator&amp;referer=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2018-19"><span>Crear un libro</span></a></li><li id="coll-download-as-rl" class="mw-list-item"><a href="/w/index.php?title=Especial:DownloadAsPdf&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=show-download-screen"><span>Descargar como PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;printable=yes" title="Versión imprimible de esta página [p]" accesskey="p"><span>Versión para imprimir</span></a></li>
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
					
					
					<div id="mw-content-text" class="mw-body-content"><div class="mw-content-ltr mw-parser-output" lang="es" dir="ltr"><div class="noprint AP rellink"><span style="font-size:88%">Artículo principal:</span>&#32;<i><a href="/wiki/Liga_de_Campeones_de_la_UEFA_2018-19" title="Liga de Campeones de la UEFA 2018-19"> Liga de Campeones de la UEFA 2018-19</a></i></div>
<p>En los <b>Octavos de final de la <a href="/wiki/Liga_de_Campeones_de_la_UEFA_2018-19" title="Liga de Campeones de la UEFA 2018-19">Liga de Campeones de la UEFA 2018-19</a></b>, participaron los dieciséis equipos que terminaron primeros y segundos de cada grupo en la fase anterior. Estos fueron distribuidos en ocho parejas. Cada pareja se enfrentó en partidos de ida y vuelta de 90 minutos cada uno. En estos encuentros regió la <a href="/wiki/Regla_del_gol_de_visitante" title="Regla del gol de visitante">regla del gol de visitante</a>, que determinó que el equipo que haya convertido más goles como visitante gana si hay empate en la diferencia de goles. En caso de que no hubiese ganador en el período regular, se realizaría una prórroga de 30 minutos, y si no hay ganador se realizarían <a href="/wiki/Tiros_desde_el_punto_penal" title="Tiros desde el punto penal">tiros desde el punto penal</a>.
</p>
<meta property="mw:PageProp/toc" />
<h2><span id="Cuadro_de_clasificaci.C3.B3n"></span><span class="mw-headline" id="Cuadro_de_clasificación">Cuadro de clasificación</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=1" title="Editar sección: Cuadro de clasificación"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="columns" style="-moz-column-count:2; -webkit-column-count:2; column-count:2;">
</div>
<center>
<table cellspacing="0" style="background: #f9f9f9; border: 1px #aaa solid; border-collapse: collapse;" width="60%">

<tbody><tr style="color:black" bgcolor="#ccddcc">
<th>Grupo
</th>
<th>Bombo 1<br />(Líderes de grupo)
</th>
<th>Bombo 2<br />(Segundos de grupo)
</th></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2018-19">A</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Atl%C3%A9tico_de_Madrid" class="mw-redirect" title="Atlético de Madrid">Atlético de Madrid</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2018-19">B</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur" class="mw-redirect" title="Tottenham Hotspur">Tottenham Hotspur</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2018-19">C</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_FC" class="mw-redirect" title="Liverpool FC">Liverpool</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2018-19">D</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/FC_Schalke_04" title="FC Schalke 04">Schalke 04</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2018-19">E</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_M%C3%BAnich" class="mw-redirect" title="Bayern Múnich">Bayern Múnich</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2018-19">F</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City" class="mw-redirect" title="Manchester City">Manchester City</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2018-19">G</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid" class="mw-redirect" title="Real Madrid">Real Madrid</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2018-19">H</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus" class="mw-redirect" title="Juventus">Juventus</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_United" class="mw-redirect" title="Manchester United">Manchester United</a>
</td></tr></tbody></table>
</center>
<h2><span class="mw-headline" id="Participantes">Participantes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=2" title="Editar sección: Participantes"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table width="100%">

<tbody><tr align="center">
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/60px-Flag_of_Portugal.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/120px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</th>
<th><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a>
</th>
<th><a href="/wiki/Par%C3%ADs_Saint-Germain" class="mw-redirect" title="París Saint-Germain">París Saint-Germain</a>
</th>
<th><a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</th>
<th><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</th>
<th><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</th>
<th><a href="/wiki/Real_Madrid" class="mw-redirect" title="Real Madrid">Real Madrid</a>
</th>
<th><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</th></tr>
<tr>
<th>
</th>
<th>Clasificado
</th>
<th>
</th>
<th>Clasificado
</th>
<th>
</th>
<th>Clasificado
</th>
<th>
</th>
<th>Clasificado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/db/Kit_left_arm_bvb1819e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ed/Kit_body_bvb1819e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e8/Kit_right_arm_bvb1819e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb1819e.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/5d/Kit_socks_bvb1819e.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_left_arm_fcbarcelona1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6c/Kit_body_fcbarcelona1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/96/Kit_right_arm_fcbarcelona1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8f/Kit_shorts_fcbarcelona1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0000BC"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbarcelona1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/e7/Kit_socks_fcbarcelona1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_cro18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/27/Kit_left_arm_cro18a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cf/Kit_body_psg1819e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_cro18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a9/Kit_right_arm_cro18a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_cro18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a4/Kit_shorts_cro18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/78/Kit_left_arm_porto1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_body_porto1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_right_arm_porto1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_porto1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/0c/Kit_socks_porto1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6d/Kit_left_arm_bayern1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#ff0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern1819h2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9f/Kit_body_bayern1819h2.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3d/Kit_right_arm_bayern1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c6/Kit_shorts_bayern1819H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bayern1819H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_socks_bayern1819H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/08/Kit_left_arm_mancity1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/40/Kit_body_mancity1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/97/Kit_right_arm_mancity1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_usa18h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_shorts_usa18h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#1C204E"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/73/Kit_socks_mancity1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5b/Kit_left_arm_realmadrid1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_body_realmadrid1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/34/Kit_right_arm_realmadrid1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8c/Kit_shorts_realmadrid1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fe/Kit_socks_realmadrid1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm.svg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/31px-Kit_left_arm.svg.png" decoding="async" width="31" height="59" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/47px-Kit_left_arm.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/62px-Kit_left_arm.svg.png 2x" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus1819home.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/03/Kit_body_juventus1819home.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm.svg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/31px-Kit_right_arm.svg.png" decoding="async" width="31" height="59" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/47px-Kit_right_arm.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/62px-Kit_right_arm.svg.png 2x" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_juventus1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e6/Kit_shorts_juventus1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/74/Kit_socks_juventus1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
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
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/60px-Flag_of_the_Netherlands.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/90px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/120px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Atl%C3%A9tico_de_Madrid" class="mw-redirect" title="Atlético de Madrid">Atlético de Madrid</a>
</th>
<th><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</th>
<th><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</th>
<th><a href="/wiki/FC_Schalke_04" title="FC Schalke 04">Schalke 04</a>
</th>
<th><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</th>
<th><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</th>
<th><a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a>
</th>
<th><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</th></tr>
<tr>
<th>
</th>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>
</th>
<th>Clasificado
</th>
<th>
</th>
<th>
</th>
<th>Clasificado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#D20000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b0/Kit_left_arm_atlmadrid1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#D20000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_cadm1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d1/Kit_body_cadm1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#D20000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_right_arm_atlmadrid1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_cadm1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/56/Kit_shorts_cadm1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_cadm1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/aa/Kit_socks_cadm1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_tottenham1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_body_tottenham1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/06/Kit_right_arm_tottenham1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#020031"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bra18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d8/Kit_shorts_bra18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/69/Kit_socks_tottenham1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3c/Kit_left_arm_liverpool1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/04/Kit_body_liverpool1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c4/Kit_right_arm_liverpool1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DD0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_socks_liverpool1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_schalke1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0e/Kit_left_arm_schalke1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_schalke1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3a/Kit_body_schalke1819H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_schalke1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e5/Kit_right_arm_schalke1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_schalke1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/aa/Kit_shorts_schalke1819H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0000FF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_schalke1819H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/5b/Kit_socks_schalke1819H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ajax1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a8/Kit_left_arm_ajax1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FD1220"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ajax1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b7/Kit_body_ajax1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ajax1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1d/Kit_right_arm_ajax1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_red.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_socks_3_stripes_red.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2b/Kit_left_arm_ol1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/33/Kit_body_ol1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0b/Kit_right_arm_ol1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/83/Kit_shorts_ol1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_ol1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4e/Kit_socks_ol1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a0/Kit_left_arm_roma1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/79/Kit_body_roma1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_right_arm_roma1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bf/Kit_shorts_roma1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#feb42f"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_roma1819H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_socks_roma1819H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#E20E0E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_left_arm_manutd1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#E20E0E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d7/Kit_body_manutd1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#E20E0E"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0d/Kit_right_arm_manutd1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/af/Kit_shorts_manutd1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_manutd1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/43/Kit_socks_manutd1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
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
<h2><span class="mw-headline" id="Estadios">Estadios</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=3" title="Editar sección: Estadios"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Signal_Iduna_Park_new_sign.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Signal_Iduna_Park_new_sign.jpg/200px-Signal_Iduna_Park_new_sign.jpg" decoding="async" width="200" height="97" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Signal_Iduna_Park_new_sign.jpg/300px-Signal_Iduna_Park_new_sign.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Signal_Iduna_Park_new_sign.jpg/400px-Signal_Iduna_Park_new_sign.jpg 2x" data-file-width="3776" data-file-height="1840" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Camp_Nou_aerial_(cropped).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Camp_Nou_aerial_%28cropped%29.jpg/200px-Camp_Nou_aerial_%28cropped%29.jpg" decoding="async" width="200" height="130" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Camp_Nou_aerial_%28cropped%29.jpg/300px-Camp_Nou_aerial_%28cropped%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Camp_Nou_aerial_%28cropped%29.jpg/400px-Camp_Nou_aerial_%28cropped%29.jpg 2x" data-file-width="1826" data-file-height="1186" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:ParcDesPrincesII.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ParcDesPrincesII.jpg/200px-ParcDesPrincesII.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ParcDesPrincesII.jpg/300px-ParcDesPrincesII.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ParcDesPrincesII.jpg/400px-ParcDesPrincesII.jpg 2x" data-file-width="1024" data-file-height="767" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Est%C3%A1dio_do_Drag%C3%A3o_(8468978586).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Est%C3%A1dio_do_Drag%C3%A3o_%288468978586%29.jpg/200px-Est%C3%A1dio_do_Drag%C3%A3o_%288468978586%29.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Est%C3%A1dio_do_Drag%C3%A3o_%288468978586%29.jpg/300px-Est%C3%A1dio_do_Drag%C3%A3o_%288468978586%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Est%C3%A1dio_do_Drag%C3%A3o_%288468978586%29.jpg/400px-Est%C3%A1dio_do_Drag%C3%A3o_%288468978586%29.jpg 2x" data-file-width="2560" data-file-height="1920" /></a></span>
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
<td><b><a href="/wiki/Signal_Iduna_Park" title="Signal Iduna Park">Signal Iduna Park</a></b><br />
<p>Ciudad: <a href="/wiki/Dortmund" title="Dortmund">Dortmund</a><br />
Capacidad: 81.360 espectadores<br />
Club: <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</p>
</td>
<td><b><a href="/wiki/Camp_Nou" title="Camp Nou">Camp Nou</a></b><br />
<p>Ciudad: <a href="/wiki/Barcelona" title="Barcelona">Barcelona</a><br />
Capacidad: <b>99.354</b> espectadores<br />
Club: <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a>
</p>
</td>
<td><b><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a></b><br />
<p>Ciudad: <a href="/wiki/Par%C3%ADs" title="París">París</a><br />
Capacidad: <b>47.500</b> espectadores<br />
Club: <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_do_Drag%C3%A3o" class="mw-redirect" title="Estadio do Dragão">Estadio do Dragão</a></b><br />
<p>Ciudad: <a href="/wiki/Oporto" title="Oporto">Oporto</a><br />
Capacidad: <b>50.033</b> espectadores<br />
Club: <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Etihad_Stadium_at_night_-_2015.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/200px-Etihad_Stadium_at_night_-_2015.jpg" decoding="async" width="200" height="105" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/300px-Etihad_Stadium_at_night_-_2015.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/400px-Etihad_Stadium_at_night_-_2015.jpg 2x" data-file-width="1024" data-file-height="537" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c8/The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg/200px-The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c8/The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg/300px-The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c8/The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg/400px-The_Santiago_Bernabeu_Stadium_-_U-g-g-B-o-y.jpg 2x" data-file-width="3264" data-file-height="2448" /></a></span>
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
<td><b><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a></b><br />
<p>Ciudad: <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>81.044</b> espectadores<br />
Club: <a href="/wiki/Real_Madrid" class="mw-redirect" title="Real Madrid">Real Madrid</a>
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
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Estadio_Wanda_Metropolitano_(2018).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/200px-Estadio_Wanda_Metropolitano_%282018%29.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/300px-Estadio_Wanda_Metropolitano_%282018%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/55/Estadio_Wanda_Metropolitano_%282018%29.jpg/400px-Estadio_Wanda_Metropolitano_%282018%29.jpg 2x" data-file-width="4896" data-file-height="3672" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Wembley-Stadion_2013_16x10.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Wembley-Stadion_2013_16x10.jpg/200px-Wembley-Stadion_2013_16x10.jpg" decoding="async" width="200" height="112" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Wembley-Stadion_2013_16x10.jpg/300px-Wembley-Stadion_2013_16x10.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Wembley-Stadion_2013_16x10.jpg/400px-Wembley-Stadion_2013_16x10.jpg 2x" data-file-width="4501" data-file-height="2524" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Panorama_of_Anfield_with_new_main_stand_(29676137824).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/200px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg" decoding="async" width="200" height="136" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/300px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/400px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 2x" data-file-width="3148" data-file-height="2143" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Veltins_Arena_T-Home_Cup.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Veltins_Arena_T-Home_Cup.jpg/200px-Veltins_Arena_T-Home_Cup.jpg" decoding="async" width="200" height="134" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Veltins_Arena_T-Home_Cup.jpg/300px-Veltins_Arena_T-Home_Cup.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Veltins_Arena_T-Home_Cup.jpg/400px-Veltins_Arena_T-Home_Cup.jpg 2x" data-file-width="1936" data-file-height="1296" /></a></span>
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
<td><b><a href="/wiki/Estadio_Metropolitano_(Madrid)" title="Estadio Metropolitano (Madrid)">Wanda Metropolitano</a></b><br />
<p>Ciudad: <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>67.703</b> espectadores<br />
Club: <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_de_Wembley" title="Estadio de Wembley">Wembley Stadium</a></b><br />
<p>Ciudad: <a href="/wiki/Londres" title="Londres">Londres</a><br />
Capacidad: <b>90.000</b> espectadores<br />
Club: <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</p>
</td>
<td><b><a href="/wiki/Anfield" title="Anfield">Anfield</a></b><br />
<p>Ciudad: <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a><br />
Capacidad: <b>54.074</b> espectadores<br />
Club: <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</p>
</td>
<td><b><a href="/wiki/Veltins-Arena" title="Veltins-Arena">Veltins-Arena</a></b><br />
<p>Ciudad: <a href="/wiki/Gelsenkirchen" title="Gelsenkirchen">Gelsenkirchen</a><br />
Capacidad: <b>60.000</b> espectadores<br />
Club: <a href="/wiki/FC_Schalke_04" title="FC Schalke 04">FC Schalke 04</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Amsterdam_Arena_Roof_Open.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Amsterdam_Arena_Roof_Open.jpg/200px-Amsterdam_Arena_Roof_Open.jpg" decoding="async" width="200" height="123" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Amsterdam_Arena_Roof_Open.jpg/300px-Amsterdam_Arena_Roof_Open.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Amsterdam_Arena_Roof_Open.jpg/400px-Amsterdam_Arena_Roof_Open.jpg 2x" data-file-width="1374" data-file-height="846" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Parc_OL.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/Parc_OL.jpg/200px-Parc_OL.jpg" decoding="async" width="200" height="112" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/Parc_OL.jpg/300px-Parc_OL.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/13/Parc_OL.jpg/400px-Parc_OL.jpg 2x" data-file-width="2592" data-file-height="1456" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Stadio_Olimpico_2008.JPG" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Stadio_Olimpico_2008.JPG/200px-Stadio_Olimpico_2008.JPG" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Stadio_Olimpico_2008.JPG/300px-Stadio_Olimpico_2008.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Stadio_Olimpico_2008.JPG/400px-Stadio_Olimpico_2008.JPG 2x" data-file-width="3264" data-file-height="2448" /></a></span>
</td>
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Old_Trafford_inside_20060726_1.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/4/43/Old_Trafford_inside_20060726_1.jpg/200px-Old_Trafford_inside_20060726_1.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/43/Old_Trafford_inside_20060726_1.jpg/300px-Old_Trafford_inside_20060726_1.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/43/Old_Trafford_inside_20060726_1.jpg/400px-Old_Trafford_inside_20060726_1.jpg 2x" data-file-width="1024" data-file-height="683" /></a></span>
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
<td><b><a href="/wiki/Johan_Cruyff_Arena" title="Johan Cruyff Arena">Johan Cruyff Arena</a></b><br />
<p>Ciudad: <a href="/wiki/%C3%81msterdam" title="Ámsterdam">Ámsterdam</a><br />
Capacidad: <b>54.990</b> espectadores<br />
Club: <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</p>
</td>
<td><b><a href="/wiki/Parc_Olympique_Lyonnais" title="Parc Olympique Lyonnais">Parc Olympique Lyonnais</a></b><br />
<p>Ciudad: <a href="/wiki/Lyon" title="Lyon">Lyon</a><br />
Capacidad: <b>59.186</b> espectadores<br />
Club: <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Ol%C3%ADmpico_de_Roma" title="Estadio Olímpico de Roma">Estadio Olímpico de Roma</a></b><br />
<p>Ciudad: <a href="/wiki/Roma" title="Roma">Roma</a><br />
Capacidad: <b>72.300</b> espectadores<br />
Club: <a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a>
</p>
</td>
<td><b><a href="/wiki/Old_Trafford" title="Old Trafford">Old Trafford</a></b><br />
<p>Ciudad: <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a><br />
Capacidad: <b>75.643</b> espectadores<br />
Club: <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</p>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Llaves">Llaves</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=4" title="Editar sección: Llaves"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
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
<td style="text-align: right;"><a href="/wiki/FC_Schalke_04" title="FC Schalke 04">Schalke 04</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">2–10
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#SCH_MCI">2–3</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MCI_SCH">0–7</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="text-align: center;">2–3
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <b><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#ATM_JUV">2–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#JUV_ATM">0–3</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;"><small>(<a href="/wiki/Regla_del_gol_de_visitante" title="Regla del gol de visitante">v</a>)</small> 3–3
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MAN_PSG">0–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#PSG_MAN">3–1</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;">4–0
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#TOT_BOR">3–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BOR_TOT">1–0</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">1–5
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <b><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LYO_BAR">0–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BAR_LYO">1–5</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="text-align: center;">3–4 <small>(<a href="/wiki/Pr%C3%B3rroga_(deporte)" title="Prórroga (deporte)">t. s.</a>)</small>
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <b><a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#ROM_POR">2–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#POR_ROM">1–3</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">5–3
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#AJA_RMA">1–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#RMA_AJA">4–1</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;">3–1
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LIV_BAY">0–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BAY_LIV">3–1</a>
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Enfrentamientos">Enfrentamientos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=5" title="Editar sección: Enfrentamientos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<h4><span id="Schalke_04_.E2.80.93_Manchester_City"></span><span class="mw-headline" id="Schalke_04_–_Manchester_City"><a href="/wiki/FC_Schalke_04" title="FC Schalke 04">Schalke 04</a> – <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=6" title="Editar sección: Schalke 04 – Manchester City"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="SCH_MCI">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 20 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/FC_Schalke_04" title="FC Schalke 04">Schalke 04</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:3</b> (2:1)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Veltins-Arena" title="Veltins-Arena">Veltins-Arena</a>,</span> <a href="/wiki/Gelsenkirchen" title="Gelsenkirchen">Gelsenkirchen</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Nabil_Bentaleb" title="Nabil Bentaleb">Bentaleb</a> <span typeof="mw:File"><span title="Anotado en el minuto 38"><img alt="Anotado en el minuto 38" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">38' </span> <span typeof="mw:File"><span title="Anotado en el minuto 45"><img alt="Anotado en el minuto 45" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">45' </span>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026845/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 18"><img alt="Anotado en el minuto 18" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">18'</small> <a href="/wiki/Sergio_Ag%C3%BCero" class="mw-redirect" title="Sergio Agüero">Agüero</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 85"><img alt="Anotado en el minuto 85" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">85'</small> <a href="/wiki/Leroy_San%C3%A9" title="Leroy Sané">Sané</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 90"><img alt="Anotado en el minuto 90" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">90'</small> <a href="/wiki/Raheem_Sterling" title="Raheem Sterling">Sterling</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 50.532 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Del_Cerro_Grande" class="mw-redirect" title="Del Cerro Grande">Del Cerro Grande</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Hern%C3%A1ndez_Hern%C3%A1ndez" class="mw-redirect" title="Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_schalke1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/01/Kit_left_arm_schalke1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_schalke1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9a/Kit_body_schalke1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_schalke1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/54/Kit_right_arm_schalke1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_schalke1819h2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/63/Kit_shorts_schalke1819h2.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0000FF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_schalke1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ec/Kit_socks_schalke1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/08/Kit_left_arm_mancity1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/40/Kit_body_mancity1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/97/Kit_right_arm_mancity1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bra18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d8/Kit_shorts_bra18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity1819h2.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b2/Kit_socks_mancity1819h2.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MCI_SCH">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 12 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>7:0 <style data-mw-deduplicate="TemplateStyles:r144106874">.mw-parser-output .sinnegrita,.mw-parser-output .sinnegrita b{font-weight:normal}</style><span class="sinnegrita">(3:0)</span></b> </div><div style="font-size: 85%">(Global <b>10:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/FC_Schalke_04" title="FC Schalke 04">Schalke 04</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a>,</span> <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Sergio_Ag%C3%BCero" class="mw-redirect" title="Sergio Agüero">Agüero</a> <span typeof="mw:File"><span title="Anotado en el minuto 35"><img alt="Anotado en el minuto 35" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">35' </span> <span typeof="mw:File"><span title="Anotado en el minuto 38"><img alt="Anotado en el minuto 38" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">38'</small><br /><a href="/wiki/Leroy_San%C3%A9" title="Leroy Sané">Sané</a> <span typeof="mw:File"><span title="Anotado en el minuto 42"><img alt="Anotado en el minuto 42" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">42'</small><br /><a href="/wiki/Raheem_Sterling" title="Raheem Sterling">Sterling</a> <span typeof="mw:File"><span title="Anotado en el minuto 55"><img alt="Anotado en el minuto 55" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">55'</small><br /><a href="/wiki/Bernardo_Silva" title="Bernardo Silva">Bernardo</a> <span typeof="mw:File"><span title="Anotado en el minuto 71"><img alt="Anotado en el minuto 71" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">71'</small><br /><a href="/wiki/Phil_Foden" title="Phil Foden">Foden</a> <span typeof="mw:File"><span title="Anotado en el minuto 78"><img alt="Anotado en el minuto 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">78'</small><br /><a href="/wiki/Gabriel_Jesus" title="Gabriel Jesus">Gabriel Jesus</a> <span typeof="mw:File"><span title="Anotado en el minuto 84"><img alt="Anotado en el minuto 84" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">84'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026855/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 51.518 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Cl%C3%A9ment_Turpin" title="Clément Turpin">Clément Turpin</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Nicolas_Rainville&amp;action=edit&amp;redlink=1" class="new" title="Nicolas Rainville (aún no redactado)">Nicolas Rainville</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/08/Kit_left_arm_mancity1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/40/Kit_body_mancity1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/97/Kit_right_arm_mancity1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bra18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d8/Kit_shorts_bra18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity1819h2.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b2/Kit_socks_mancity1819h2.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#96FF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_schalke041819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c3/Kit_left_arm_schalke041819t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#96FF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_schalke041819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_body_schalke041819t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#96FF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_schalke041819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/38/Kit_right_arm_schalke041819t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#96FF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_schalke041819t1.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/61/Kit_shorts_schalke041819t1.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#96FF00"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_schalke041819t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/d/de/Kit_socks_schalke041819t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td></tr></tbody></table>
<h4><span id="Atl.C3.A9tico_de_Madrid_.E2.80.93_Juventus"></span><span class="mw-headline" id="Atlético_de_Madrid_–_Juventus"><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a> – <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=7" title="Editar sección: Atlético de Madrid – Juventus"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="ATM_JUV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 20 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:0</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Metropolitano_(Madrid)" title="Estadio Metropolitano (Madrid)">Wanda Metropolitano</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Jos%C3%A9_Mar%C3%ADa_Gim%C3%A9nez" title="José María Giménez">Giménez</a> <span typeof="mw:File"><span title="Anotado en el minuto 78"><img alt="Anotado en el minuto 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">78'</small><br /><a href="/wiki/Diego_God%C3%ADn" title="Diego Godín">Godín</a> <span typeof="mw:File"><span title="Anotado en el minuto 83"><img alt="Anotado en el minuto 83" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">83'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026846/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 59.673 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Felix_Zwayer" title="Felix Zwayer">Felix Zwayer</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bastian_Dankert" title="Bastian Dankert">Bastian Dankert</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#D20000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b0/Kit_left_arm_atlmadrid1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#D20000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4a/Kit_body_atlmadrid1819H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#D20000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_right_arm_atlmadrid1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atlmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cc/Kit_shorts_atlmadrid1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_atlmadrid1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_socks_atlmadrid1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#28262d"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_juve1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a4/Kit_left_arm_juve1819T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juve1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e1/Kit_body_juve1819T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#28262d"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_juve1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1b/Kit_right_arm_juve1819T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_juventus1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3c/Kit_shorts_juventus1819t.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juve1819t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/3d/Kit_socks_juve1819t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="JUV_ATM">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 12 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:0)</span></b> </div><div style="font-size: 85%">(Global <b>3:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Club_Atl%C3%A9tico_de_Madrid" title="Club Atlético de Madrid">Atlético de Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Juventus_Stadium" title="Juventus Stadium">Allianz Stadium</a>,</span> <a href="/wiki/Tur%C3%ADn" title="Turín">Turín</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Cristiano_Ronaldo" title="Cristiano Ronaldo">Ronaldo</a> <span typeof="mw:File"><span title="Anotado en el minuto 27"><img alt="Anotado en el minuto 27" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">27'</small> <span typeof="mw:File"><span title="Anotado en el minuto 49"><img alt="Anotado en el minuto 49" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">49'</small> <span typeof="mw:File"><span title="Anotado en el minuto 86"><img alt="Anotado en el minuto 86" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">86' </span>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026856/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 40.884 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Bj%C3%B6rn_Kuipers" title="Björn Kuipers">Björn Kuipers</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_juventus1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8f/Kit_body_juventus1819H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_juventus1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e6/Kit_shorts_juventus1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_juventus1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/74/Kit_socks_juventus1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_atlmadrid1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/65/Kit_left_arm_atlmadrid1819t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_atlmadrid1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/62/Kit_body_atlmadrid1819t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_atlmadrid1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_right_arm_atlmadrid1819t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0477B4"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_atlmadrid1819t2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/da/Kit_shorts_atlmadrid1819t2.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0000FF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_cadm1819h2.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/68/Kit_socks_cadm1819h2.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a></b>
</td></tr></tbody></table>
<h4><span id="Manchester_United_.E2.80.93_Par.C3.ADs_Saint-Germain"></span><span class="mw-headline" id="Manchester_United_–_París_Saint-Germain"><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a> – <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=8" title="Editar sección: Manchester United – París Saint-Germain"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MAN_PSG">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 12 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:2</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Old_Trafford" title="Old Trafford">Old Trafford</a>,</span> <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026849/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 53"><img alt="Anotado en el minuto 53" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">53'</small> <a href="/wiki/Presnel_Kimpembe" title="Presnel Kimpembe">Kimpembe</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 60"><img alt="Anotado en el minuto 60" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">60'</small> <a href="/wiki/Kylian_Mbapp%C3%A9" title="Kylian Mbappé">Mbappé</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 74.054 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Daniele_Orsato" title="Daniele Orsato">Daniele Orsato</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_left_arm_manutd1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d7/Kit_body_manutd1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0d/Kit_right_arm_manutd1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_manutd1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/af/Kit_shorts_manutd1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_manutd1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/43/Kit_socks_manutd1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_usa18h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c4/Kit_left_arm_usa18h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg1819f.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4d/Kit_body_psg1819f.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_usa18h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a6/Kit_right_arm_usa18h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_usa18h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_shorts_usa18h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="PSG_MAN">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 6 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:3 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:2)</span></b> </div><div style="font-size: 85%">(Global <b>3:3</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a>,</span> <a href="/wiki/Par%C3%ADs" title="París">París</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Juan_Bernat" title="Juan Bernat">Bernat</a> <span typeof="mw:File"><span title="Anotado en el minuto 12"><img alt="Anotado en el minuto 12" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">12'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026859/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 2"><img alt="Anotado en el minuto 2" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">2'</small> <span typeof="mw:File"><span title="Anotado en el minuto 30"><img alt="Anotado en el minuto 30" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">30'</small> <a href="/wiki/Romelu_Lukaku" title="Romelu Lukaku">Lukaku</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 90+4"><img alt="Anotado en el minuto 90+4" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">90+4' </span> <a href="/wiki/Marcus_Rashford" title="Marcus Rashford">Rashford</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 47.441 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Slovenia.svg" class="mw-file-description" title="Bandera de Eslovenia"><img alt="Bandera de Eslovenia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/20px-Flag_of_Slovenia.svg.png" decoding="async" width="20" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/30px-Flag_of_Slovenia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/40px-Flag_of_Slovenia.svg.png 2x" data-file-width="1200" data-file-height="600" /></a></span></span> <a href="/wiki/Damir_Skomina" title="Damir Skomina">Damir Skomina</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_cro18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/27/Kit_left_arm_cro18a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cf/Kit_body_psg1819e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_cro18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a9/Kit_right_arm_cro18a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_cro18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a4/Kit_shorts_cro18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#F2D3DB"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_manutd1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/38/Kit_left_arm_manutd1819a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#F2D3DB"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_manutd1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/dc/Kit_body_manutd1819a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#F2D3DB"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_manutd1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/84/Kit_right_arm_manutd1819a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_manutd1819a2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a3/Kit_shorts_manutd1819a2.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#F2D3DB"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_manutd1819a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/8c/Kit_socks_manutd1819a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a></b>
</td></tr></tbody></table>
<h4><span id="Tottenham_Hotspur_.E2.80.93_Borussia_Dortmund"></span><span class="mw-headline" id="Tottenham_Hotspur_–_Borussia_Dortmund"><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a> – <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=9" title="Editar sección: Tottenham Hotspur – Borussia Dortmund"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="TOT_BOR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 13 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:0</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_de_Wembley" title="Estadio de Wembley">Wembley Stadium</a>,</span> <a href="/wiki/Londres" title="Londres">Londres</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Son_Heung-Min" class="mw-redirect" title="Son Heung-Min">Son</a> <span typeof="mw:File"><span title="Anotado en el minuto 47"><img alt="Anotado en el minuto 47" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">47'</small><br /><a href="/wiki/Jan_Vertonghen" title="Jan Vertonghen">Vertonghen</a> <span typeof="mw:File"><span title="Anotado en el minuto 83"><img alt="Anotado en el minuto 83" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">83'</small><br /><a href="/wiki/Fernando_Llorente" title="Fernando Llorente">Llorente</a> <span typeof="mw:File"><span title="Anotado en el minuto 86"><img alt="Anotado en el minuto 86" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">86'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026850/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 71.214 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Antonio_Miguel_Mateu_Lahoz" class="mw-redirect" title="Antonio Miguel Mateu Lahoz">Mateu Lahoz</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_tottenham1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_body_tottenham1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/06/Kit_right_arm_tottenham1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#020031"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bra18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d8/Kit_shorts_bra18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/69/Kit_socks_tottenham1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/db/Kit_left_arm_bvb1819e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ed/Kit_body_bvb1819e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e8/Kit_right_arm_bvb1819e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb1819e.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/5d/Kit_socks_bvb1819e.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BOR_TOT">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 5 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div><div style="font-size: 85%">(Global <b>0:4</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Signal_Iduna_Park" title="Signal Iduna Park">Signal Iduna Park</a>,</span> <a href="/wiki/Dortmund" title="Dortmund">Dortmund</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026860/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 48"><img alt="Anotado en el minuto 48" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">48'</small> <a href="/wiki/Harry_Kane" title="Harry Kane">Kane</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 66.099 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Pol_van_Boekel" title="Pol van Boekel">Pol van Boekel</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/db/Kit_left_arm_bvb1819e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ed/Kit_body_bvb1819e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb1819e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e8/Kit_right_arm_bvb1819e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb1819e.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/5d/Kit_socks_bvb1819e.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_tottenham1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_body_tottenham1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/06/Kit_right_arm_tottenham1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#020031"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bra18a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d8/Kit_shorts_bra18a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/69/Kit_socks_tottenham1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a></b>
</td></tr></tbody></table>
<h4><span id="Olympique_de_Lyon_.E2.80.93_Barcelona"></span><span class="mw-headline" id="Olympique_de_Lyon_–_Barcelona"><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a> – <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=10" title="Editar sección: Olympique de Lyon – Barcelona"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LYO_BAR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 19 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:0</b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Parc_Olympique_Lyonnais" title="Parc Olympique Lyonnais">Parc Olympique Lyonnais</a>,</span> <a href="/wiki/Lyon" title="Lyon">Lyon</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026851/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 57.889 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/wiki/C%C3%BCneyt_%C3%87ak%C4%B1r" title="Cüneyt Çakır">Cüneyt Çakır</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2b/Kit_left_arm_ol1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/33/Kit_body_ol1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0b/Kit_right_arm_ol1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ol1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/83/Kit_shorts_ol1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_ol1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/4e/Kit_socks_ol1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#DDFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcbarcelona1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/21/Kit_left_arm_fcbarcelona1819a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#DDFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcbarcelona1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/38/Kit_body_fcbarcelona1819a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#DDFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcbarcelona1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/54/Kit_right_arm_fcbarcelona1819a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DDFF00"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DDFF00"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbarcelona1819a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_socks_fcbarcelona1819a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BAR_LYO">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 13 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>5:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(2:0)</span></b> </div><div style="font-size: 85%">(Global <b>5:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Olympique_de_Lyon" title="Olympique de Lyon">Olympique de Lyon</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Camp_Nou" title="Camp Nou">Camp Nou</a>,</span> <a href="/wiki/Barcelona" title="Barcelona">Barcelona</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Lionel_Messi" title="Lionel Messi">Messi</a> <span typeof="mw:File"><span title="Anotado en el minuto 17"><img alt="Anotado en el minuto 17" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">17' </span> <span typeof="mw:File"><span title="Anotado en el minuto 78"><img alt="Anotado en el minuto 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">78'</small><br /><a href="/wiki/Philippe_Coutinho" title="Philippe Coutinho">Coutinho</a> <span typeof="mw:File"><span title="Anotado en el minuto 31"><img alt="Anotado en el minuto 31" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">31'</small><br /><a href="/wiki/Gerard_Piqu%C3%A9" title="Gerard Piqué">Piqué</a> <span typeof="mw:File"><span title="Anotado en el minuto 81"><img alt="Anotado en el minuto 81" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">81'</small><br /><a href="/wiki/Ousmane_Demb%C3%A9l%C3%A9" title="Ousmane Dembélé">Dembélé</a> <span typeof="mw:File"><span title="Anotado en el minuto 86"><img alt="Anotado en el minuto 86" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">86'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026857/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 58"><img alt="Anotado en el minuto 58" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">58'</small> <a href="/wiki/Lucas_Tousart" title="Lucas Tousart">Tousart</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 92.346 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/w/index.php?title=Pawe%C5%82_Raczkowski&amp;action=edit&amp;redlink=1" class="new" title="Paweł Raczkowski (aún no redactado)">Paweł Raczkowski</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_left_arm_fcbarcelona1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6c/Kit_body_fcbarcelona1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/96/Kit_right_arm_fcbarcelona1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_fcbarcelona1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8f/Kit_shorts_fcbarcelona1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0000BC"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcbarcelona1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/e7/Kit_socks_fcbarcelona1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF6600"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ol1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e4/Kit_left_arm_ol1819T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF6600"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ol1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/28/Kit_body_ol1819T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF6600"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ol1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f0/Kit_right_arm_ol1819T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF6600"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ol1819T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8d/Kit_shorts_ol1819T.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF6600"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_ol1819T.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/3e/Kit_socks_ol1819T.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></b>
</td></tr></tbody></table>
<h4><span id="Roma_.E2.80.93_Porto"></span><span class="mw-headline" id="Roma_–_Porto"><a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a> – <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=11" title="Editar sección: Roma – Porto"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="ROM_POR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 12 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:1</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Ol%C3%ADmpico_de_Roma" title="Estadio Olímpico de Roma">Estadio Olímpico de Roma</a>,</span> <a href="/wiki/Roma" title="Roma">Roma</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Nicol%C3%B2_Zaniolo" title="Nicolò Zaniolo">Zaniolo</a> <span typeof="mw:File"><span title="Anotado en el minuto 70"><img alt="Anotado en el minuto 70" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">70'</small> <span typeof="mw:File"><span title="Anotado en el minuto 76"><img alt="Anotado en el minuto 76" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">76'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026852/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 79"><img alt="Anotado en el minuto 79" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">79'</small> <a href="/wiki/Adri%C3%A1n_L%C3%B3pez_%C3%81lvarez" title="Adrián López Álvarez">Adrián</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 51.727 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Pol_van_Boekel" title="Pol van Boekel">Pol van Boekel</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a0/Kit_left_arm_roma1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/79/Kit_body_roma1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_right_arm_roma1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bf/Kit_shorts_roma1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#feb42f"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_roma1819H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_socks_roma1819H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/78/Kit_left_arm_porto1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_body_porto1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_right_arm_porto1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_porto1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/0c/Kit_socks_porto1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="POR_ROM">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 6 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(2:1, 1:0)</span></b> <span style="font-size: 85%">(<a href="/wiki/Pr%C3%B3rroga_(deporte)" title="Prórroga (deporte)">t.&#160;s.</a>)</span></div><div style="font-size: 85%">(Global <b>4:3</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Associazione_Sportiva_Roma" title="Associazione Sportiva Roma">Roma</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_do_Drag%C3%A3o" class="mw-redirect" title="Estadio do Dragão">Estadio do Dragão</a>,</span> <a href="/wiki/Oporto" title="Oporto">Oporto</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Tiquinho_Soares" title="Tiquinho Soares">Soares</a> <span typeof="mw:File"><span title="Anotado en el minuto 26"><img alt="Anotado en el minuto 26" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">26'</small><br /><a href="/wiki/Moussa_Marega" title="Moussa Marega">Marega</a> <span typeof="mw:File"><span title="Anotado en el minuto 52"><img alt="Anotado en el minuto 52" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">52'</small><br /><a href="/wiki/Alex_Telles" title="Alex Telles">Telles</a> <span typeof="mw:File"><span title="Anotado en el minuto 117"><img alt="Anotado en el minuto 117" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">117' </span>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026858/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 37"><img alt="Anotado en el minuto 37" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Penal"><img alt="Penal" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/10px-Penal.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/15px-Penal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Penal.svg/20px-Penal.svg.png 2x" data-file-width="280" data-file-height="280" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">37' </span> <a href="/wiki/Daniele_De_Rossi" title="Daniele De Rossi">De Rossi</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 49.029 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/wiki/C%C3%BCneyt_%C3%87ak%C4%B1r" title="Cüneyt Çakır">Cüneyt Çakır</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/78/Kit_left_arm_porto1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_body_porto1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_porto1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_right_arm_porto1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_porto1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/0/0c/Kit_socks_porto1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a0/Kit_left_arm_roma1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/79/Kit_body_roma1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/57/Kit_right_arm_roma1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_roma1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bf/Kit_shorts_roma1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#feb42f"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_roma1819H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/ba/Kit_socks_roma1819H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a></b>
</td></tr></tbody></table>
<h4><span id="Ajax_.E2.80.93_Real_Madrid"></span><span class="mw-headline" id="Ajax_–_Real_Madrid"><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a> – <a href="/wiki/Real_Madrid" class="mw-redirect" title="Real Madrid">Real Madrid</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=12" title="Editar sección: Ajax – Real Madrid"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="AJA_RMA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 13 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:2</b> (0:0)<b> </b></div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid" class="mw-redirect" title="Real Madrid">Real Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Johan_Cruyff_Arena" title="Johan Cruyff Arena">Johan Cruyff Arena</a>,</span> <a href="/wiki/%C3%81msterdam" title="Ámsterdam">Ámsterdam</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Hakim_Ziyech" title="Hakim Ziyech">Ziyech</a> <span typeof="mw:File"><span title="Anotado en el minuto 75"><img alt="Anotado en el minuto 75" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">75'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026847/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 60"><img alt="Anotado en el minuto 60" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">60'</small> <a href="/wiki/Karim_Benzema" title="Karim Benzema">Benzema</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 87"><img alt="Anotado en el minuto 87" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">87'</small> <a href="/wiki/Marco_Asensio" title="Marco Asensio">Asensio</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 52.286 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Slovenia.svg" class="mw-file-description" title="Bandera de Eslovenia"><img alt="Bandera de Eslovenia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/20px-Flag_of_Slovenia.svg.png" decoding="async" width="20" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/30px-Flag_of_Slovenia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/40px-Flag_of_Slovenia.svg.png 2x" data-file-width="1200" data-file-height="600" /></a></span></span> <a href="/wiki/Damir_Skomina" title="Damir Skomina">Damir Skomina</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_ajax1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a8/Kit_left_arm_ajax1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FD1220"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ajax1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b7/Kit_body_ajax1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_ajax1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1d/Kit_right_arm_ajax1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_red.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_socks_3_stripes_red.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_left_arm_realmadrid1819a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0000FF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/37/Kit_body_realmadrid1819a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#ff0001"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/34/Kit_right_arm_realmadrid1819a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#fffiff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/72/Kit_shorts_realmadrid1819a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0000FF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid1819a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_socks_realmadrid1819a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="RMA_AJA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 5 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Real_Madrid" class="mw-redirect" title="Real Madrid">Real Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:4 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:2)</span></b> </div><div style="font-size: 85%">(Global <b>3:5</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Marco_Asensio" title="Marco Asensio">Asensio</a> <span typeof="mw:File"><span title="Anotado en el minuto 70"><img alt="Anotado en el minuto 70" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">70'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026853/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 7"><img alt="Anotado en el minuto 7" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">7'</small> <a href="/wiki/Hakim_Ziyech" title="Hakim Ziyech">Ziyech</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 18"><img alt="Anotado en el minuto 18" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">18'</small> <a href="/wiki/David_Neres" title="David Neres">Neres</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 62"><img alt="Anotado en el minuto 62" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">62'</small> <a href="/wiki/Du%C5%A1an_Tadi%C4%87" title="Dušan Tadić">Tadić</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 72"><img alt="Anotado en el minuto 72" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">72'</small> <a href="/wiki/Lasse_Sch%C3%B8ne" title="Lasse Schøne">Schøne</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 77.013 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Felix_Brych" title="Felix Brych">Felix Brych</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bastian_Dankert" title="Bastian Dankert">Bastian Dankert</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5b/Kit_left_arm_realmadrid1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_body_realmadrid1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/34/Kit_right_arm_realmadrid1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadrid1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8c/Kit_shorts_realmadrid1819h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadrid1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fe/Kit_socks_realmadrid1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_ajax1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/92/Kit_body_ajax1819a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_ajax1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e4/Kit_shorts_ajax1819a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_ajax1819a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ed/Kit_socks_ajax1819a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a></b>
</td></tr></tbody></table>
<h4><span id="Liverpool_.E2.80.93_Bayern_M.C3.BAnich"></span><span class="mw-headline" id="Liverpool_–_Bayern_Múnich"><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a> – <a href="/wiki/Bayern_M%C3%BAnich" class="mw-redirect" title="Bayern Múnich">Bayern Múnich</a></span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=13" title="Editar sección: Liverpool – Bayern Múnich"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h4>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LIV_BAY">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida, 19 de febrero de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:0</b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_M%C3%BAnich" class="mw-redirect" title="Bayern Múnich">Bayern Múnich</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Anfield" title="Anfield">Anfield</a>,</span> <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026848/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 52.250 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Gianluca_Rocchi" title="Gianluca Rocchi">Gianluca Rocchi</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3c/Kit_left_arm_liverpool1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/04/Kit_body_liverpool1819h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool1819h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c4/Kit_right_arm_liverpool1819h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DD0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DD0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_liverpool1819h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_socks_liverpool1819h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern1819A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/12/Kit_left_arm_bayern1819A.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern1819A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e1/Kit_body_bayern1819A.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern1819A.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_right_arm_bayern1819A.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern1819a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c9/Kit_shorts_bayern1819a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bayern1819A.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/8d/Kit_socks_bayern1819A.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BAY_LIV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta, 13 de marzo de 2019, 21:00 <a href="/wiki/Hora_central_europea" title="Hora central europea">HEC</a>;
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Bayern_M%C3%BAnich" class="mw-redirect" title="Bayern Múnich">Bayern Múnich</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:3 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:1)</span></b> </div><div style="font-size: 85%">(Global <b>1:3</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a>,</span> <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">
</td>
<td valign="top" align="right"><a href="/wiki/Joel_Matip" title="Joel Matip">Matip</a> <span typeof="mw:File"><span title="Anotado en el minuto 39"><img alt="Anotado en el minuto 39" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span><span style="position:relative; left:-5px;"><span typeof="mw:File"><span title="Autogol"><img alt="Autogol" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/22/Red_circle_thick.svg/10px-Red_circle_thick.svg.png" decoding="async" width="10" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/22/Red_circle_thick.svg/15px-Red_circle_thick.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/22/Red_circle_thick.svg/20px-Red_circle_thick.svg.png 2x" data-file-width="250" data-file-height="250" /></span></span></span><span style="font-size: 10px; vertical-align: middle;">39' </span>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/season=2019/matches/round=2000981/match=2026854/index.html?iv=true">Reporte</a>
</td>
<td valign="top" align="left"><span typeof="mw:File"><span title="Anotado en el minuto 26"><img alt="Anotado en el minuto 26" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">26'</small> <span typeof="mw:File"><span title="Anotado en el minuto 84"><img alt="Anotado en el minuto 84" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">84'</small> <a href="/wiki/Sadio_Man%C3%A9" title="Sadio Mané">Mané</a><br /><span typeof="mw:File"><span title="Anotado en el minuto 69"><img alt="Anotado en el minuto 69" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">69'</small> <a href="/wiki/Virgil_van_Dijk" title="Virgil van Dijk">Van Dijk</a>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 68.145 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Daniele_Orsato" title="Daniele Orsato">Daniele Orsato</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6d/Kit_left_arm_bayern1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#ff0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern1819h2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9f/Kit_body_bayern1819h2.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3d/Kit_right_arm_bayern1819H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern1819H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c6/Kit_shorts_bayern1819H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bayern1819H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_socks_bayern1819H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#E6EBE9"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/42/Kit_left_arm_liverpool1819t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#E6EBE9"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/26/Kit_body_liverpool1819t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#E6EBE9"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool1819t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/92/Kit_right_arm_liverpool1819t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#E6EBE9"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#E6EBE9"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<table cellspacing="0" width="100%">

<tbody><tr>
<td align="center"><b>Pasa a cuartos de final<br /><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></b>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Clasificados_para_Cuartos_de_Final">Clasificados para Cuartos de Final</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=14" title="Editar sección: Clasificados para Cuartos de Final"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table align="center" cellpadding="2" cellspacing="0" style="background: #f5faff; border: 1px #aaa solid; border-collapse: collapse; font-size: 95%;" width="80%">

<tbody><tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/45px-Flag_of_Italy.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/68px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Juventus_de_Tur%C3%ADn" title="Juventus de Turín">Juventus</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Manchester_United_Football_Club" title="Manchester United Football Club">Manchester United</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a></b>
</td></tr>
<tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/45px-Flag_of_Portugal.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/68px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/68px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/90px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/F%C3%BAtbol_Club_Barcelona" title="Fútbol Club Barcelona">Barcelona</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Ajax_de_%C3%81msterdam" title="Ajax de Ámsterdam">Ajax</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a></b>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Referencias">Referencias</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=15" title="Editar sección: Referencias"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="listaref" style="list-style-type: decimal;"></div>
<h2><span id="V.C3.A9ase_tambi.C3.A9n"></span><span class="mw-headline" id="Véase_también">Véase también</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=16" title="Editar sección: Véase también"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/Anexo:Ronda_preliminar_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Ronda preliminar de la Liga de Campeones de la UEFA 2018-19">Anexo: Ronda preliminar de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Anexo:Primera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Primera ronda previa de la Liga de Campeones de la UEFA 2018-19">Anexo: Primera ronda previa de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Anexo:Segunda_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Segunda ronda previa de la Liga de Campeones de la UEFA 2018-19">Anexo: Segunda ronda previa de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Anexo:Tercera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Tercera ronda previa de la Liga de Campeones de la UEFA 2018-19">Anexo: Tercera ronda previa de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Anexo:Cuarta_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Cuarta ronda previa de la Liga de Campeones de la UEFA 2018-19">Anexo: Cuarta ronda previa de la Liga de Campeones de la UEFA 2018-19</a></li>
<li>Fase de grupos <small>(<a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2018-19">Grupo A</a>, <a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2018-19">Grupo B</a>, <a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2018-19">Grupo C</a>, <a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2018-19">Grupo D</a>, <a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2018-19">Grupo E</a>, <a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2018-19">Grupo F</a>, <a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2018-19">Grupo G</a>, <a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2018-19">Grupo H</a>)</small></li>
<li><a class="mw-selflink selflink">Anexo: Octavos de final de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Anexo:Cuartos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Cuartos de final de la Liga de Campeones de la UEFA 2018-19">Anexo: Cuartos de final de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Anexo:Semifinales_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Anexo:Semifinales de la Liga de Campeones de la UEFA 2018-19">Anexo: Semifinales de la Liga de Campeones de la UEFA 2018-19</a></li>
<li><a href="/wiki/Final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19" title="Final de la Liga de Campeones de la UEFA 2018-19">Final de la Liga de Campeones de la UEFA 2018-19</a></li></ul>
<h2><span class="mw-headline" id="Enlaces_externos">Enlaces externos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;action=edit&amp;section=17" title="Editar sección: Enlaces externos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://es.uefa.com/uefachampionsleague/index.html">Página oficial de la UEFA Champions League</a></li></ul>
<p><br clear="all" />
</p>
<table class="wikitable" border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; margin:0 auto;">

<tbody><tr style="text-align: center;">
<td width="30%">Predecesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2017-18" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2017-18">2017-18</a></b>
</td>
<td width="40%"><b>Octavos de final de la<br /><a href="/wiki/Liga_de_Campeones_de_la_UEFA" title="Liga de Campeones de la UEFA">Liga de Campeones de la UEFA</a></b><br />2018-19
</td>
<td width="30%">Sucesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2019-20" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2019-20">2019-20</a></b>
</td></tr></tbody></table>
<!-- 
NewPP limit report
Parsed by mw‐api‐int.codfw.main‐774c7d5bcb‐f8zng
Cached time: 20240212175230
Cache expiry: 2592000
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.772 seconds
Real time usage: 0.959 seconds
Preprocessor visited node count: 25068/1000000
Post‐expand include size: 260017/2097152 bytes
Template argument size: 99330/2097152 bytes
Highest expansion depth: 14/100
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 1504/5000000 bytes
Lua time usage: 0.052/10.000 seconds
Lua memory usage: 1773568/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  400.207      1 -total
 65.69%  262.892     16 Plantilla:Partidos
 19.89%   79.609     88 Plantilla:Bandera
 18.14%   72.594     64 Plantilla:En_varias_líneas
  8.97%   35.885     16 Plantilla:Str_sub
  8.73%   34.950     32 Plantilla:Trim
  8.59%   34.378     32 Plantilla:Árbitro
  8.54%   34.169    128 Plantilla:Bandera_icono
  7.86%   31.453     32 Plantilla:Football_kit
  6.83%   27.325     43 Plantilla:Gol
-->

<!-- Saved in parser cache with key eswiki:pcache:idhash:8742721-0!canonical and timestamp 20240212175229 and revision id 154931376. Rendering was triggered because: api-parse
 -->
</div><!--esi <esi:include src="/esitest-fa8a495983347898/content" /> --><noscript><img src="https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" width="1" height="1" style="border: none; position: absolute;"></noscript>
<div class="printfooter" data-nosnippet="">Obtenido de «<a dir="ltr" href="https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;oldid=154931376">https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;oldid=154931376</a>»</div></div>
					<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Especial:Categor%C3%ADas" title="Especial:Categorías">Categoría</a>: <ul><li><a href="/wiki/Categor%C3%ADa:Liga_de_Campeones_de_la_UEFA_2018-19" title="Categoría:Liga de Campeones de la UEFA 2018-19">Liga de Campeones de la UEFA 2018-19</a></li></ul></div></div>
				</div>
			</main>
			
		</div>
		<div class="mw-footer-container">
			
<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info">
	<li id="footer-info-lastmod"> Esta página se editó por última vez el 29 oct 2023 a las 00:25.</li>
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
	<li id="footer-places-mobileview"><a href="//es.m.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2018-19&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Versión para móviles</a></li>
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
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgHostname":"mw1452","wgBackendResponseTime":108,"wgPageParseReport":{"limitreport":{"cputime":"0.772","walltime":"0.959","ppvisitednodes":{"value":25068,"limit":1000000},"postexpandincludesize":{"value":260017,"limit":2097152},"templateargumentsize":{"value":99330,"limit":2097152},"expansiondepth":{"value":14,"limit":100},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":1504,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  400.207      1 -total"," 65.69%  262.892     16 Plantilla:Partidos"," 19.89%   79.609     88 Plantilla:Bandera"," 18.14%   72.594     64 Plantilla:En_varias_líneas","  8.97%   35.885     16 Plantilla:Str_sub","  8.73%   34.950     32 Plantilla:Trim","  8.59%   34.378     32 Plantilla:Árbitro","  8.54%   34.169    128 Plantilla:Bandera_icono","  7.86%   31.453     32 Plantilla:Football_kit","  6.83%   27.325     43 Plantilla:Gol"]},"scribunto":{"limitreport-timeusage":{"value":"0.052","limit":"10.000"},"limitreport-memusage":{"value":1773568,"limit":52428800}},"cachereport":{"origin":"mw-api-int.codfw.main-774c7d5bcb-f8zng","timestamp":"20240212175230","ttl":2592000,"transientcontent":false}}});});</script>
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
		row_data.append('18/19')
			
		tabla_data.append(row_data)
		print(tabla_data)

	#Especicificar nombre del csv donde guardar la tabla
	file_name = 'octavos.csv'
	with open(file_name, 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(tabla_data)
	print(f'Se guardó la tabla en {file_name}')

else:
	print('No se encontró la tabla')